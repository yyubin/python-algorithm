import sys
n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
window = sum(li[:m])
res = window
for i in range(m, n):
    window += li[i] - li[i-m]
    res = max(res, window)
print(res)