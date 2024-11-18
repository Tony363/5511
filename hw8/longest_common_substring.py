def lcsstr_length(X, Y):
    m, n = len(X), len(Y)
    c = [[0] * (n + 1) for _ in range(m + 1)]
    maxLength = 0
    maxI = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                if c[i][j] > maxLength:
                    maxLength = c[i][j]
                    maxI = i
            else:
                c[i][j] = 0
    return maxLength, maxI, c

def print_lcsstr(X, maxI, maxLength):
    return X[maxI - maxLength:maxI]

if __name__ == "__main__":
    # Testing Cases
    test_cases = [
        ("abcdef", "zabcf"),
        ("abcdxyz", "xyzabcd"),
        ("zxabcdezy", "yzabcdezx"),
        ("abc", "def"),
        ("", "abc"),
        ("abc", ""),
        ("aaaaa", "aaa"),
        ("abcde", "abfde"),
        ("abcXYZabc", "XYZabcabc"),
        ("ABABC", "BABCA"),
        # no common substring
        # both string identical
        
    ]

    for X, Y in test_cases:
        maxLength, maxI, c = lcsstr_length(X, Y)
        substring = print_lcsstr(X, maxI, maxLength) if maxLength > 0 else ""
        print(f"Input X: '{X}', Y: '{Y}'")
        print(f"Longest Common Substring: '{substring}'")
        print(f"Length: {maxLength}")
        print("Table c:")
        for row in c:
            print(row)
        print("-" * 50)
