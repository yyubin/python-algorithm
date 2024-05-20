import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]


def bfs(x, y):
    q = deque([(x, y, 1)])
    visited[x][y] = True

    while q:
        xx, yy, cnt = q.popleft()
        for dx, dy in d:
            ddx = dx + xx
            ddy = dy + yy

            if 0 <= ddx < n and 0 <= ddy < m and not visited[ddx][ddy]:
                visited[ddx][ddy] = True
                if graph[ddx][ddy] == 0:
                    q.append((ddx, ddy, cnt + 1))
                else:
                    return cnt

ans = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            visited = [[False] * m for _ in range(n)]
            ans = max(ans, bfs(i, j))

print(ans)

