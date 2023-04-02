import sys

def kmp(all_string, pattern):
    global count
    table = [0 for _ in range(len(pattern))]
    i = 0
    for j in range(1, len(pattern)):
        while i > 0 and pattern[i] != pattern[j]:
            i = table[i-1]

        if pattern[i] == pattern[j]:
            i += 1
            table[j] = i

    i = 0
    for j in range(len(all_string)):
        while i > 0 and pattern[i] != all_string[j]:
            i = table[i-1]

        if pattern[i] == all_string[j]:
            i += 1
            if i == len(pattern):
                count += 1
                result.append(j-i+1+1)
                i = table[i-1]



count = 0
result = []
t = sys.stdin.readline().rstrip()
p = sys.stdin.readline().rstrip()

kmp(t, p)
print(count)
print(*result)


#KMP 문자열 알고리즘
# https://yiyj1030.tistory.com/495
