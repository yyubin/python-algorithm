import sys
from collections import defaultdict
n, k = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

res = 0
counter = defaultdict(int)
left = 0
for i in range(n):
    counter[li[i]] += 1
    while counter[li[i]] > k:
        counter[li[left]] -= 1
        left += 1
    res = max(res, i - left + 1)
print(res)

# 투포인터+슬라이딩윈도우

