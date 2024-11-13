#!/usr/bin/env python
"""Find the longest repeated substring.
"Efficient way to find longest duplicate string for Python (From Programming Pearls)"
http://stackoverflow.com/questions/13560037/
The algorithm is based on "Prefix doubling".
The worst time complexity is O(n (log n)^2). Memory requirements are linear.
"""

import time

from random import randint
import itertools
import sys
import unittest
from itertools import groupby
from operator import itemgetter
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
try:
    log.addHandler(logging.NullHandler())
except AttributeError:
    pass


def run():
    if sys.argv[1:] == ['-']:
        text = sys.stdin.read()
    elif sys.argv[1:]:
        print('Reading data...')
        text = open(sys.argv[1]).read()
    else:
        text = 'banana'
    print('Sorting...')
    result = longest_common_substring(text)
    print('Longest common substrings in "{0}..." are:\n{1}'.format(
          text[:20], result))


def longest_common_substring(text):
    """Get the longest common substrings and their positions.
    >>> longest_common_substring('banana')
    {'ana': [1, 3]}
    >>> text = "not so Agamemnon, who spoke fiercely to "
    >>> sorted(longest_common_substring(text).items())
    [(' s', [3, 21]), ('no', [0, 13]), ('o ', [5, 20, 38])]
    This function can be easy modified for any criteria, e.g. for searching ten
    longest non overlapping repeated substrings.
    """
    sa, rsa, lcp = suffix_array(text)
    maxlen = max(lcp)
    result = {}
    for i in range(1, len(text)):
        if lcp[i] == maxlen:
            j1, j2, h = sa[i - 1], sa[i], lcp[i]
            assert text[j1:j1 + h] == text[j2:j2 + h]
            substring = text[j1:j1 + h]
            if substring not in result:
                result[substring] = [j1]
            result[substring].append(j2)
    return dict((k, sorted(v)) for k, v in result.items())


def suffix_array(text, _step=16):
    """Analyze all common strings in the text.
    Short substrings of the length _step a are first pre-sorted. The are the
    results repeatedly merged so that the garanteed number of compared
    characters bytes is doubled in every iteration until all substrings are
    sorted exactly.
    Arguments:
        text:  The text to be analyzed.
        _step: Is only for optimization and testing. It is the optimal length
               of substrings used for initial pre-sorting. The bigger value is
               faster if there is enough memory. Memory requirements are
               approximately (estimate for 32 bit Python 3.3):
                   len(text) * (29 + (_size + 20 if _size > 2 else 0)) + 1MB
    Return value:      (tuple)
      (sa, rsa, lcp)
        sa:  Suffix array                  for i in range(1, size):
               assert text[sa[i-1]:] < text[sa[i]:]
        rsa: Reverse suffix array          for i in range(size):
               assert rsa[sa[i]] == i
        lcp: Longest common prefix         for i in range(1, size):
               assert text[sa[i-1]:sa[i-1]+lcp[i]] == text[sa[i]:sa[i]+lcp[i]]
               if sa[i-1] + lcp[i] < len(text):
                   assert text[sa[i-1] + lcp[i]] < text[sa[i] + lcp[i]]
    >>> suffix_array(text='banana')
    ([5, 3, 1, 0, 4, 2], [3, 2, 5, 1, 4, 0], [0, 1, 3, 0, 0, 2])
    Explanation: 'a' < 'ana' < 'anana' < 'banana' < 'na' < 'nana'
    The Longest Common String is 'ana': lcp[2] == 3 == len('ana')
    It is between  tx[sa[1]:] == 'ana' < 'anana' == tx[sa[2]:]
    """
    tx = text
    t0 = time.time()
    size = len(tx)
    step = min(max(_step, 1), len(tx))
    sa = list(range(len(tx)))
    log.debug('%6.3f pre sort', time.time() - t0)
    sa.sort(key=lambda i: tx[i:i + step])
    log.debug('%6.3f after sort', time.time() - t0)
    grpstart = size * [False] + [True]  # a boolean map for iteration speedup.
    # It helps to skip yet resolved values. The last value True is a sentinel.
    rsa = size * [None]
    stgrp, igrp = '', 0
    for i, pos in enumerate(sa):
        st = tx[pos:pos + step]
        if st != stgrp:
            grpstart[igrp] = (igrp < i - 1)
            stgrp = st
            igrp = i
        rsa[pos] = igrp
        sa[i] = pos
    grpstart[igrp] = (igrp < size - 1 or size == 0)
    log.debug('%6.3f after group', time.time() - t0)
    while grpstart.index(True) < size:
        # assert step <= size
        nmerge = 0
        nextgr = grpstart.index(True)
        while nextgr < size:
            igrp = nextgr
            nextgr = grpstart.index(True, igrp + 1)
            glist = []
            for ig in range(igrp, nextgr):
                pos = sa[ig]
                if rsa[pos] != igrp:
                    break
                newgr = rsa[pos + step] if pos + step < size else -1
                glist.append((newgr, pos))
            glist.sort()
            for ig, g in groupby(glist, key=itemgetter(0)):
                g = [x[1] for x in g]
                sa[igrp:igrp + len(g)] = g
                grpstart[igrp] = (len(g) > 1)
                for pos in g:
                    rsa[pos] = igrp
                igrp += len(g)
            nmerge += len(glist)
        log.debug('%6.3f for step=%d nmerge=%d', time.time() - t0, step, nmerge)
        step *= 2
    del grpstart
    # create LCP array
    lcp = size * [None]
    h = 0
    for i in range(size):
        if rsa[i] > 0:
            j = sa[rsa[i] - 1]
            while i != size - h and j != size - h and tx[i + h] == tx[j + h]:
                h += 1
            lcp[rsa[i]] = h
            if h > 0:
                h -= 1
    if size > 0:
        lcp[0] = 0
    log.debug('%6.3f end', time.time() - t0)
    return sa, rsa, lcp

# ---


class TestMixin(object):
    def suffix_verify(self, text, step=16):
        tx = text
        sa, rsa, lcp = suffix_array(text=tx, _step=step)
        self.assertEqual(set(sa), set(range(len(tx))))
        ok = True
        for i0, i1, h in zip(sa[:-1], sa[1:], lcp[1:]):
            self.assertEqual(tx[i1:i1 + h], tx[i0:i0 + h], "Verify LCP characters equal on text '%s...'" % text[:20])
            self.assertGreater(tx[i1 + h:i1 + h + 1], tx[i0 + h:i0 + h + 1],
                               "Verify LCP+1 char is different '%s...'" % text[:20])
            self.assertLessEqual(max(i0, i1), len(tx) - h,
                                 "Verify LCP is not more than length of string '%s...'" % text[:20])
        self.assertTrue(ok)


class SuffixArrayTest(unittest.TestCase, TestMixin):
    def test_16(self):
        # 'a' < 'ana' < 'anana' < 'banana' < 'na' < 'nana'
        expect = ([5, 3, 1, 0, 4, 2], [3, 2, 5, 1, 4, 0], [0, 1, 3, 0, 0, 2])
        self.assertEqual(suffix_array(text='banana', _step=16), expect)

    def test_1(self):
        expect = ([5, 3, 1, 0, 4, 2], [3, 2, 5, 1, 4, 0], [0, 1, 3, 0, 0, 2])
        self.assertEqual(suffix_array(text='banana', _step=1), expect)

    def test_mini(self):
        self.assertEqual(suffix_array(text='', _step=1), ([], [], []))
        self.assertEqual(suffix_array(text='a', _step=1), ([0], [0], [0]))
        self.assertEqual(suffix_array(text='aa', _step=1), ([1, 0], [1, 0], [0, 1]))
        self.assertEqual(suffix_array(text='aaa', _step=1), ([2, 1, 0], [2, 1, 0], [0, 1, 2]))

    def test_example(self):
        self.suffix_verify('abracadabra')

    def test_cartesian(self):
        """Test all combinations of alphabet "ABC" up to length 4 characters"""
        for size in range(7):
            for cartesian in itertools.product(*(size * ['ABC'])):
                text = ''.join(cartesian)
                log.debug('Testing "%s"', text)
                self.suffix_verify(text, 1)

    def test_lcp(self):
        expect = {'ana': [1, 3]}
        self.assertDictEqual(longest_common_substring('banana'), expect)
        expect = {' s': [3, 21], 'no': [0, 13], 'o ': [5, 20, 38]}
        self.assertDictEqual(longest_common_substring(
             "not so Agamemnon, who spoke fiercely to "), expect)


class SlowTests(unittest.TestCase, TestMixin):
    """Slow development tests running many minutes.
    It can be run only by an EXPLICIT command!
        e.g.: python -m unittest maxsubstring.SlowTests._test_random
    """
    def _test_random(self):
        for power in range(2, 21, 2):
            size = randint(2 ** (power - 1), 2 ** power)
            for alphabet in (2, 4, 16, 256):
                text = ''.join(chr(65 + randint(0, alphabet - 1)) for _ in range(size))
                log.debug('%s %s %s', size, alphabet, 1)
                self.suffix_verify(text, 1)
                log.debug('%s %s %s', size, alphabet, 16)
                self.suffix_verify(text, 16)


if __name__ == '__main__':
    """https://gist.github.com/pombredanne/b3637b88301568508b1168a11cfad062
    """
    run()
