import sys
from collections import defaultdict
n, k = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
d = defaultdict(int)
left = 0
res = 0
for i in range(n):
    d[li[i]] += 1
    while d[li[i]] > k:
        d[li[left]] -= 1
        left += 1
    res = max(res, i - left + 1)
print(res)

