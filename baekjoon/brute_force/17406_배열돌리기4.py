import sys
from itertools import permutations
from copy import deepcopy
n, m, k = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

calculate = []
for _ in range(k):
    calculate.append(list(map(int, sys.stdin.readline().split())))

result = sys.maxsize
for p in permutations(calculate, k):
    copy_ = deepcopy(graph)
    for r, c, s in p:
        r -= 1
        c -= 1
        for n in range(s, 0, -1):
            tmp = copy_[r-n][c+n]
            copy_[r-n][c-n+1:c+n+1] = copy_[r-n][c-n:c+n]
            for row in range(r-n, r+n):
                copy_[row][c-n] = copy_[row+1][c-n]
            copy_[r+n][c-n:c+n] = copy_[r+n][c-n+1:c+n+1]
            for row in range(r+n, r-n, -1):
                copy_[row][c+n] = copy_[row-1][c+n]
            copy_[r-n+1][c+n] = tmp

    for row in copy_:
        result = min(result, sum(row))

print(result)
