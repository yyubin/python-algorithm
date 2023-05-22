import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def ice_melt(x, y):
    cnt = 0
    for k in range(4):
        ddx = x + dx[k]
        ddy = y + dy[k]
        if 0 <= ddx < n and 0 <= ddy < m and graph[ddx][ddy] == 0:
            cnt += 1
    re_graph[x][y] = max(0, graph[x][y] - cnt)


def bfs(x, y):
    q = deque()
    visited[x][y] = True
    q.append((x, y))

    while q:
        xx, yy = q.popleft()
        for i in range(4):
            ddx = xx + dx[i]
            ddy = yy + dy[i]
            if 0 <= ddx < n and 0 <= ddy < m and not visited[ddx][ddy]:
                if graph[ddx][ddy] != 0:
                    q.append((ddx, ddy))
                    visited[ddx][ddy] = True


block = 0
year = 0
flag = False
visited = [[False] * m for _ in range(n)]

while True:
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and not visited[i][j]:
                block += 1
                bfs(i, j)
                flag = True

    if block >= 2:
        break
    if not flag:
        year = 0
        break

    year += 1

    re_graph = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                ice_melt(i, j)

    graph = re_graph

    block = 0
    flag = False
    visited = [[False] * m for _ in range(n)]

print(year)

