import sys
n, k = map(int, sys.stdin.readline().split())
ice = [0] * 1000001
idx = 0
for _ in range(n):
    a, b = map(int, sys.stdin.readline().strip().split())
    ice[b] = a
    idx = max(idx, b)
size = (2*k) + 1
window = sum(ice[:size])
res = window
for i in range(size, idx+1):
    window += ice[i] - ice[i-size]
    res = max(res, window)
print(res)
