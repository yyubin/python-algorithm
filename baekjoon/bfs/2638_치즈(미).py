import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

res = 0

def find_cheese():
    q = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                q.append((i, j))

    return q

def find_melt(q):
    result = []
    while q:
        x, y = q.popleft()
        tmp = 0

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < n and 0 <= yy < m:
                if graph[xx][yy] == 0:
                    tmp += 1

        if tmp >= 2:
            result.append((x, y))

    return result


while True:

    cheese = find_cheese()
    if not cheese:
        print(res)
        break

    melt_cheese = find_melt(cheese)

    for x, y in melt_cheese:
        graph[x][y] = 0

    res += 1



