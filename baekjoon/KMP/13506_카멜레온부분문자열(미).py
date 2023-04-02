import sys


def kmp(pattern):
    global count
    table = [0] * len(pattern)
    i = 0

    for j in range(1, len(pattern)):
        while i > 0 and pattern[i] != pattern[j]:
            i = table[i - 1]
        if pattern[i] == pattern[j]:
            count += 1
            i += 1
            table[j] = i

    return table


string = sys.stdin.readline().rstrip()
count = 0
tmp = kmp(string)

li = list(string)
li2 = list(string)

print(count)
result = li[:tmp[-1]]
print(result)

li2.pop()
li2.pop(0)

# if "".join(result) in "".join(li2):
#     print("".join(result))
# else:
#     print(-1)

