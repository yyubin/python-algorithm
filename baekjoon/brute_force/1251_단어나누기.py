import sys
from itertools import combinations
st = sys.stdin.readline().rstrip()
n = [x for x in range(1, len(st))]
ans = []
for x, y in combinations(n, 2):
    s1 = st[:x][::-1]
    s2 = st[x:y][::-1]
    s3 = st[y:][::-1]
    ans.append(''.join(s1+s2+s3))

ans.sort()
print(ans[0])

# 1이상 n 이하
# [:x]
# [x:y]
# [y:]

