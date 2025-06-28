import sys
from collections import defaultdict
for _ in range(int(sys.stdin.readline())):
    n, k = map(int, sys.stdin.readline().split())
    li = list(map(int, sys.stdin.readline().split()))
    d = defaultdict(list)

    for i in range(n):
        if len(d[li[i]]) < k:
            d[li[i]].append(i)

    res = []
    for i in d.values():
        res.extend(i)

    paint = (len(res) // k) * k
    ans = [0] * n
    for i in range(paint):
        ans[res[i]] = (i%k) + 1

    print(*ans)
