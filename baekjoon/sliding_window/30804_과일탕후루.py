import sys
from collections import defaultdict
n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
counter = defaultdict(int)
left = 0
res = 0
for i in range(n):
    counter[s[i]] += 1
    while len(counter) > 2:
        counter[s[left]] -= 1
        if counter[s[left]] == 0:
            del counter[s[left]]
        left += 1
    res = max(res, i-left+1)
print(res)
