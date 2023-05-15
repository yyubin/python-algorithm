import sys
from collections import deque

dx, dy, dz = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]

def bfs(z, x, y):
    q = deque()
    visited[z][x][y] = 0
    q.append((z, x, y))

    while q:
        zz, xx, yy = q.popleft()
        for k in range(6):
            ddz = zz + dz[k]
            ddx = xx + dx[k]
            ddy = yy + dy[k]
            if 0 <= ddz < l and 0 <= ddx < r and 0 <= ddy < c:
                if visited[ddz][ddx][ddy] == -1 and graph[ddz][ddx][ddy] == '.':
                    q.append((ddz, ddx, ddy))
                    visited[ddz][ddx][ddy] = visited[zz][xx][yy] + 1
                if graph[ddz][ddx][ddy] == 'E':
                    print(f"Escaped in {visited[zz][xx][yy] + 1} minute(s).")
                    return

    print("Trapped!")



while True:
    l, r, c = map(int, sys.stdin.readline().split())

    if l == r == c == 0:
        break

    visited = [[[-1] * c for _ in range(r)] for _ in range(l)]
    graph = []
    for _ in range(l):
        tmp = []
        for _ in range(r):
            tmp.append(list(sys.stdin.readline().rstrip()))
        graph.append(tmp)
        dummy = sys.stdin.readline()

    for i in range(l):
        for j in range(r):
            for u in range(c):
                if graph[i][j][u] == 'S':
                    bfs(i, j, u)

