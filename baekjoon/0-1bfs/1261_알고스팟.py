import sys
from collections import deque
m, n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
dist = [[float('inf')] * m for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs():
    q = deque()
    q.append((0, 0))
    dist[0][0] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                cost = graph[nx][ny]
                if dist[nx][ny] > dist[x][y] + cost:
                    dist[nx][ny] = dist[x][y] + cost
                    if cost == 0:
                        q.appendleft((nx, ny))
                    else:
                        q.append((nx, ny))

    return dist[n-1][m-1]

print(bfs())