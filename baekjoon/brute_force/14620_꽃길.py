import sys
from itertools import combinations
n = int(sys.stdin.readline())
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
li = [(x, y) for x in range(1, n-1) for y in range(1, n-1)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
res = sys.maxsize

for tmp in combinations(li, 3):
    visited = []
    total = 0
    flag = False
    for x, y in tmp:
        visited.append((x, y))
        total += cost[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx, ny) not in visited:
                visited.append((nx, ny))
                total += cost[nx][ny]
            else:
                flag = True
                break
        if flag:
            total = sys.maxsize
            break

    res = min(res, total)

print(res)
