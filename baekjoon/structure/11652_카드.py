import sys
from collections import defaultdict
n = int(sys.stdin.readline())
cnt = defaultdict(int)

for _ in range(n):
    a = int(sys.stdin.readline())
    cnt[a] += 1

cnt = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))
print(cnt[0][0])
