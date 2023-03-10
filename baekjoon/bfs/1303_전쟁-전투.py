import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = []
visited = [[False] * (n+1) for _ in range(m)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

for _ in range(m):
    graph.append(list(sys.stdin.readline().rstrip()))

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    tmp_cnt = 1

    while q:
        xx, yy = q.popleft()
        for k in range(4):
            ddx = xx + dx[k]
            ddy = yy + dy[k]
            if 0 <= ddx < m and 0 <= ddy < n and not visited[ddx][ddy]:
                if graph[xx][yy] == graph[ddx][ddy]:
                    q.append((ddx, ddy))
                    visited[ddx][ddy] = True
                    tmp_cnt += 1
    return tmp_cnt

cnt_w = []
cnt_b = []
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            cnt = bfs(i, j)
            if graph[i][j] == 'W':
                cnt_w.append(cnt**2)
            else:
                cnt_b.append(cnt**2)


print(sum(cnt_w), sum(cnt_b))
