import sys
n, k = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
prefix = [li[0]] + [0] * (n-1)
for i in range(1, n):
    prefix[i] = li[i] + prefix[i-1]
prefix.sort()
res = 0
for _ in range(k):
    res += prefix.pop()
print(res)