import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

num = [0] * n

idx = 0
i = 0
while idx != n:
    for j in range(n):
        if i+1 == li[j]:
            num[j] = idx
            idx += 1
    i += 1
print(*num)

