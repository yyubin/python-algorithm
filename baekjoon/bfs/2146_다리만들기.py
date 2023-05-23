import sys
from collections import deque
n = int(sys.stdin.readline())
graph = []
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

def land_check(x, y, num):
    visited = [[False] * n for _ in range(n)]
    graph[x][y] = num
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        xx, yy = q.popleft()
        for k in range(4):
            ddx = xx + dx[k]
            ddy = yy + dy[k]
            if 0 <= ddx < n and 0 <= ddy < n and not visited[ddx][ddy] and graph[ddx][ddy] == 1:
                graph[ddx][ddy] = num
                q.append((ddx, ddy))
                visited[ddx][ddy] = True
def bfs(x, y, now):
    visited = [[-1] * n for _ in range(n)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 0

    while q:
        xx, yy = q.popleft()
        for k in range(4):
            ddx = xx + dx[k]
            ddy = yy + dy[k]
            if 0 <= ddx < n and 0 <= ddy < n and visited[ddx][ddy] == -1:
                if graph[ddx][ddy] == 0:
                    q.append((ddx, ddy))
                    visited[ddx][ddy] = visited[xx][yy] + 1
                elif graph[ddx][ddy] != now:
                    return visited[xx][yy]
    return sys.maxsize


result = sys.maxsize
land = 2
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            land_check(i, j, land)
            land += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            result = min(result, bfs(i, j, graph[i][j]))

print(result)
