import sys
from itertools import combinations
n = int(sys.stdin.readline())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = [0] * n

for i, v in enumerate(li):
    for tmp in combinations(v, 3):
        ans[i] = max(sum(tmp)%10, ans[i])

a = 0
res = max(ans)
for i in range(n):
    if ans[i] == res:
        a = i

print(a+1)

