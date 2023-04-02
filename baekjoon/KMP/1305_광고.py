import sys


def kmp(pattern):
    table = [0] * len(pattern)
    i = 0

    for j in range(1, len(pattern)):
        while i > 0 and pattern[i] != pattern[j]:
            i = table[i - 1]
        if pattern[i] == pattern[j]:
            i += 1
            table[j] = i
    i = l-1-table[l-1]
    print(i+1)


l = int(sys.stdin.readline())
string = sys.stdin.readline().rstrip()
kmp(string)

