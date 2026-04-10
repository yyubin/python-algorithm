import bisect
import sys
n = int(sys.stdin.readline())
t = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))

d = [0] * (n+1)

for i in range(1, n+1):
    idx = bisect.bisect_left(t, t[i-1] - b[i-1])
    d[i] = max(c[i-1] + d[idx], d[i-1])
print(d[n])
#
# while start <= end:
#     mid = (start + end) // 2
#     chk(mid)
#     start = end + 1
#


