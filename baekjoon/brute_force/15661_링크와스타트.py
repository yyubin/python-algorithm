import sys
from itertools import combinations
n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ans = sys.maxsize

for i in range(1, n):
    for comb in combinations(range(n), i):
        team = set(range(n))
        teamA = set(comb)
        teamB = team - teamA

        tmpA = 0
        for x in teamA:
            for y in teamA:
                tmpA += graph[x][y]

        tmpB = 0
        for x in teamB:
            for y in teamB:
                tmpB += graph[x][y]

        ans = min(abs(tmpA-tmpB), ans)

print(ans)
