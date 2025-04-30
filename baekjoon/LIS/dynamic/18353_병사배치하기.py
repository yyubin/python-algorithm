import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
d = [1] * n

for i in range(n):
    for j in range(i):
        if li[i] < li[j]:
            d[i] = max(d[i], d[j]+1)

print(len(li) - max(d))
