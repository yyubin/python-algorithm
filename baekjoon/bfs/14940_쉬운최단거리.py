import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
visited = [[False] * m for _ in range(n)]

def bfs(x, y):
    q = deque([(x, y, 1)])
    visited[x][y] = True
    graph[x][y] = 0

    while q:
        xx, yy, c = q.popleft()
        for k in range(4):
            ddx = xx + dx[k]
            ddy = yy + dy[k]
            if 0 <= ddx < n and 0 <= ddy < m and not visited[ddx][ddy] and graph[ddx][ddy] == 1:
                visited[ddx][ddy] = True
                graph[ddx][ddy] = c
                q.append((ddx, ddy, c+1))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2 and not visited[i][j]:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            graph[i][j] = -1

for i in graph:
    print(*i)
