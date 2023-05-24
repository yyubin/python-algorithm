import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
graph = []

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

visited = [[[0] * m for _ in range(n)] for _ in range(k+1)]


def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1

    while q:
        cnt, x, y = q.popleft()
        if x == n - 1 and y == m - 1:
            print(visited[cnt][x][y])
            return
        for i in range(4):
            ddx = dx[i] + x
            ddy = dy[i] + y
            if 0 <= ddx < n and 0 <= ddy < m:
                if graph[ddx][ddy] == 0 and visited[cnt][ddx][ddy] == 0:
                    visited[cnt][ddx][ddy] = visited[cnt][x][y] + 1
                    q.append((cnt, ddx, ddy))
                elif graph[ddx][ddy] == 1 and cnt < k and visited[cnt+1][ddx][ddy] == 0:
                    visited[cnt + 1][ddx][ddy] = visited[cnt][x][y] + 1
                    q.append((cnt + 1, ddx, ddy))

    print(-1)

bfs()
