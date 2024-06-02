import sys
from itertools import combinations
n = int(sys.stdin.readline())
mem = list(range(n))
stat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

res = sys.maxsize
for comb1 in combinations(mem, n//2):
    a, b = 0, 0
    comb2 = list(set(mem) - set(comb1))

    for i in combinations(comb1, 2):
        a += stat[i[0]][i[1]]
        a += stat[i[1]][i[0]]

    for i in combinations(comb2, 2):
        b += stat[i[0]][i[1]]
        b += stat[i[1]][i[0]]

    res = min(res, abs(a-b))

print(res)


