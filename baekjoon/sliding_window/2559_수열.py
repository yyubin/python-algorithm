import sys
n, k = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
now = sum(li[:k])
res = now
for i in range(n-k):
    now += li[i+k] - li[i]
    res = max(res, now)
print(res)
