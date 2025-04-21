import sys
from collections import deque

dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
visited = [[False] * n for _ in range(m)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    count = 1

    while q:
        ddx, ddy = q.popleft()
        for i in range(4):
            if graph[ddx][ddy] & (2 ** i) == 0:
                nx = ddx + dx[i]
                ny = ddy + dy[i]
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    count += 1

    return count

res1 = 0
res2 = 0
for a in range(m):
    for b in range(n):
        if not visited[a][b]:
            res2 = max(res2, bfs(a, b))
            res1 += 1

print(res1)
print(res2)

res3 = 0
for a in range(m):
    for b in range(n):
        for k in range(4):
            if graph[a][b] & (2 ** k) != 0:
                visited = [[False] * n for _ in range(m)]
                graph[a][b] -= (2 ** k)
                res3 = max(bfs(a, b), res3)
                graph[a][b] += (2 ** k)

print(res3)
