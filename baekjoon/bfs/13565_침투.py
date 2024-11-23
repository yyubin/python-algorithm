import sys
from collections import deque
m, n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(m)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
visited = [[False] * n for _ in range(m)]

def bfs(x, y):
    q = deque()
    visited[x][y] = True
    q.append((x, y))

    while q:
        xx, yy = q.popleft()
        for k in range(4):
            ddx = xx + dx[k]
            ddy = yy + dy[k]
            if 0 <= ddx < m and 0 <= ddy < n and not visited[ddx][ddy] and graph[ddx][ddy] == 0:
                visited[ddx][ddy] = True
                q.append((ddx, ddy))

for i, v in enumerate(graph[0]):
    if v == 0:
        bfs(0, i)

print('NO' if True not in visited[m-1] else 'YES')


