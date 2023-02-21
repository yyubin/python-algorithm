import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

start = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            start.append((i, j))


def bfs(start):
    q = deque()
    for x, y in start:
        q.append((x, y))
        visited[x][y] = True

    while q:
        x, y = q.popleft()
        for k in range(4):
            ddx = dx[k] + x
            ddy = dy[k] + y
            if 0 <= ddx < n and 0 <= ddy < m:
                if not visited[ddx][ddy] and graph[ddx][ddy] == 0:
                    visited[ddx][ddy] = True
                    graph[ddx][ddy] = graph[x][y] + 1
                    q.append((ddx, ddy))


bfs(start)

max_ = 0
flag = True
for i in range(n):
    if not flag:
        break
    for j in range(m):
        tmp = graph[i][j]
        if tmp == 0:
            print(-1)
            flag = False
            break
        max_ = max(tmp, max_)

else:
    print(max_ - 1)
