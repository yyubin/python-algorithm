import sys
from collections import deque
m, n, k = map(int, sys.stdin.readline().split())
graph = [[0] * n for _ in range(m)]
visited = [[False] * n for _ in range(m)]


for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    cnt = 1
    while q:
        xx, yy = q.popleft()
        for i in range(4):
            ddx = xx + dx[i]
            ddy = yy + dy[i]
            if 0 <= ddx < m and 0 <= ddy < n:
                if not visited[ddx][ddy] and graph[ddx][ddy] == 0:
                    q.append((ddx, ddy))
                    visited[ddx][ddy] = True
                    cnt += 1

    return cnt


result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0 and not visited[i][j]:
            result.append(bfs(i, j))

print(len(result))
result.sort()
print(*result)