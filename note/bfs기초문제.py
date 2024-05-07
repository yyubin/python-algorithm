import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

visited = [[False] * m for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

ice_cream = 0

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            ddx = now_x + dx[i]
            ddy = now_y + dy[i]
            if 0 <= ddx < n and 0 <= ddy < m:
                if graph[ddx][ddy] == 0 and not visited[ddx][ddy]:
                    q.append((ddx, ddy))
                    visited[ddx][ddy] = True


for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and not visited[i][j]:
            bfs(i, j)
            ice_cream += 1

print(ice_cream)
