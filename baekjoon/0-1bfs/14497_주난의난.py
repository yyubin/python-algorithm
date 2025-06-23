import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
graph = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]
dist = [[float('inf')] * m for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

dist[x1-1][y1-1] = 0
graph[x1-1][y1-1] = 0
q = deque([(x1-1, y1-1)])

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == '#':
                print(dist[x][y] + 1)
                sys.exit()
            cost = int(graph[nx][ny])
            if dist[nx][ny] > dist[x][y] + cost:
                dist[nx][ny] = dist[x][y] + cost
                if cost == 0:
                    q.appendleft((nx, ny))
                else:
                    q.append((nx, ny))


