import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(str, sys.stdin.readline())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
cnt = 0


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    global cnt

    while q:
        xx, yy = q.popleft()
        for k in range(4):
            ddx = xx + dx[k]
            ddy = yy + dy[k]

            if 0 <= ddx < n and 0 <= ddy < m and not visited[ddx][ddy]:
                visited[ddx][ddy] = True
                if graph[ddx][ddy] == 'P':
                    cnt += 1
                    q.append((ddx, ddy))
                elif graph[ddx][ddy] == 'O':
                    q.append((ddx, ddy))


for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            bfs(i, j)

print('TT' if cnt == 0 else cnt)

