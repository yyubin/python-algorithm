import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
for _ in range(n):
    graph.append(list(sys.stdin.readline()))

def bfs(x, y):
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    q = deque()
    q.append((x, y))

    while q:
        xx, yy = q.popleft()
        for k in range(4):
            ddx = xx + dx[k]
            ddy = yy + dy[k]
            if 0 <= ddx < n and 0 <= ddy < m and graph[ddx][ddy] == 'L' and visited[ddx][ddy] == 0:
                visited[ddx][ddy] = visited[xx][yy] + 1
                q.append((ddx, ddy))

    max_ = 0
    for v in visited:
        max_ = max(max_, max(v))

    return max_

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            result = max(result, bfs(i, j))

print(result-1)

