import sys

def kmp(pattern):
    table = [0] * len(pattern)
    i = 0
    for j in range(1, len(pattern)):
        while i > 0 and pattern[i] != pattern[j]:
            i = table[i-1]

        if pattern[i] == pattern[j]:
            i += 1
            table[j] = i
    return max(table)



string = sys.stdin.readline().rstrip()
result = 0

for i in range(len(string)):
    result = max(result, kmp(string[i:len(string)]))

print(result)

