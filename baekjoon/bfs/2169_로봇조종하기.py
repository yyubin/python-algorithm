import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = []
visited = [[0] * n for _ in range(m)]
dx, dy = [-1, 1, 0], [0, 0, -1]

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = graph[0][0]

    while q:
        x, y = q.popleft()
        if x == m and y == n:
            break
        for i in range(3):
            ddx = x + dx[i]
            ddy = y + dy[i]
            if 0 <= ddx < m and 0 <= ddy < n and visited[ddx][ddy] == 0:
                visited[ddx][ddy] = visited[x][y] + graph[ddx][ddy]
                q.append((ddx, ddy))


bfs()
result = 0
for j in visited:
    result = max(result, max(j))

print(result)

