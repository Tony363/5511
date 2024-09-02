import random
import time
import numpy as np


def insertion_sort(
    a:list,
    n:int,
    ops_insert:int=0
)->list:
    for i in range(1,n):
        k = a[i]
        j = i - 1
        while j >= 0 and a[j] > k:
            a[j + 1] = a[j]
            ops_insert += 1
            j = j - 1
        a[j + 1] = k
    print("OPERATIONS FOR INSERTION - ",ops_insert)
    return a

def merge(
    a:list, 
    p:int, 
    q:int, 
    r:int,
    ops_merge:int
)->None:
    nl = q - p + 1  # Number of elements in left subarray
    nr = r - q      # Number of elements in right subarray
    left = [0] * nl
    right = [0] * nr

    for i in range(nl):
        left[i] = a[p + i]
        ops_merge += 1
    for j in range(nr):
        right[j] = a[q + j + 1]
        ops_merge += 1

    i = j = 0
    k = p
    while i < nl and j < nr:
        ops_merge += 1
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1

    # Copy remaining elements of left, if any
    while i < nl:
        a[k] = left[i]
        i += 1
        k += 1

    # Copy remaining elements of right, if any
    while j < nr:
        a[k] = right[j]
        j += 1
        k += 1
    return ops_merge

def merge_sort(
    a:list, 
    p:int, 
    r:int,
    ops_merge:int=0
)->list:
    if p >= r:
        return
    q = (p + r) // 2
    merge_sort(a, p, q)
    merge_sort(a, q + 1, r)
    ops_merge += merge(a, p, q, r,ops_merge=ops_merge)
    print("MERGE SORT OPERATION COUNT - ",ops_merge)
    return a



if __name__ == "__main__":
    n = 10
    arr = [random.randint(0, n) for i in range(n)]
    print(insertion_sort(arr, n))
    print(merge_sort(arr, 0, n - 1))
    # print(time_complexity_and_operations(insertion_sort, arr))
    # print(time_complexity_and_operations(merge_sort, arr))