import sys
from collections import deque
m, n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
dx, dy = [1, -1, 0, 0, 1, 1, -1, -1], [0, 0, 1, -1, 1, -1, 1, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        xx, yy = q.popleft()
        for i in range(8):
            ddx = xx + dx[i]
            ddy = yy + dy[i]
            if 0 <= ddx < m and 0 <= ddy < n and not visited[ddx][ddy] and graph[ddx][ddy] == 1:
                visited[ddx][ddy] = True
                q.append((ddx, ddy))

cnt = 0
for i in range(m):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            bfs(i, j)
            cnt += 1

print(cnt)