import sys
from itertools import combinations
n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
li.sort()
used = []
result = []

for cb in combinations(li, m):
    if cb in used:
        continue
    used.append(cb)

    if m == 1:
        result.append(cb)
        continue

    flag, st = True, cb[0]
    for i in range(1, len(cb)):
        if st > cb[i]:
            flag = False
            break
        st = cb[i]

    if flag:
        result.append(cb)

for i in result:
    print(*i)

