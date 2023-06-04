import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())

graph = []
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

move = {0: (0, -1), 1: (-1, 0), 2: (0, 1), 3: (1, 0)}


for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))


def bfs(x, y, direction):
    cnt = 0
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        xx, yy = q.popleft()
        cnt += 1
        for k in range(4):
            pass
        ddx, ddy = move[direction]
        ddx += xx
        ddy += yy
        if 0 <= ddx < m and 0 <= ddy < n and graph[ddx][ddy] != 1 and not visited[ddx][ddy]:
            pass




