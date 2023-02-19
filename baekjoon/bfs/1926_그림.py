import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []
visited = [[False] * m for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
queue = deque()

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

max_ = 0

def bfs(nx, ny):
    global max_
    queue.append((nx, ny))
    visited[nx][ny] = True
    cnt = 1
    while queue:
        x, y = queue.popleft();
        for k in range(4):
            ddx = dx[k] + x
            ddy = dy[k] + y
            if 0 <= ddx < n and 0 <= ddy < m:
                if graph[ddx][ddy] == 1 and not visited[ddx][ddy]:
                    cnt += 1
                    visited[ddx][ddy] = True
                    queue.append((ddx, ddy))

    max_ = max(max_, cnt)
    return 1

pic_cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            pic_cnt += bfs(i, j)

print(pic_cnt)
print(max_)

