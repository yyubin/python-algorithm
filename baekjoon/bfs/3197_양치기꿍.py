import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
visited = [[False] * c for _ in range(r)]
sheep = 0
wolf = 0


def bfs(x, y):
    alive_sheep = 0
    alive_wolf = 0

    q = deque()
    q.append((x, y))
    visited[x][y] = True

    if graph[x][y] == 'v':
        alive_wolf += 1
    if graph[x][y] == 'k':
        alive_sheep += 1

    while q:
        xx, yy = q.popleft()
        for k in range(4):
            ddx = xx + dx[k]
            ddy = yy + dy[k]

            if 0 <= ddx < r and 0 <= ddy < c and not visited[ddx][ddy] and graph[ddx][ddy] != '#':
                visited[ddx][ddy] = True
                if graph[ddx][ddy] == 'k':
                    alive_sheep += 1
                elif graph[ddx][ddy] == 'v':
                    alive_wolf += 1
                q.append((ddx, ddy))

    if alive_sheep > alive_wolf:
        return alive_sheep, 0
    else:
        return 0, alive_wolf


for i in range(r):
    for j in range(c):
        if graph[i][j] != '#' and not visited[i][j]:
            result = bfs(i, j)
            sheep += result[0]
            wolf += result[1]

print(sheep, wolf)
