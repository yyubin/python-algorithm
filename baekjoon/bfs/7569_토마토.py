import sys
from collections import deque
m, n, h = map(int, sys.stdin.readline().split())
graph = []
q = deque([])

for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, sys.stdin.readline().split())))
        for k in range(m):
            if tmp[j][k] == 1:
                q.append([i, j, k])
    graph.append(tmp)

dx, dy, dz = [-1, 1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]

while q:
    x, y, z = q.popleft()

    for f in range(6):
        a = x + dx[f]
        b = y + dy[f]
        c = z + dz[f]

        if 0 <= a < h and 0 <= b < n and 0 <= c < m:
            if graph[a][b][c] == 0:
                q.append((a, b, c))
                graph[a][b][c] = graph[x][y][z] + 1

result = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                sys.exit()
        result = max(result, max(j))

print(result - 1)



# def bfs():
#     global cnt, m, n, k
#
#     for i in range(k):
#         for j in range(n):
#             for k in range(m):
#                 if graph[k][j][i] == 1:
#                     q.append((k, j, i))
#
#     while q:
#         xx, yy, zz = q.popleft()
#         for k in range(2):
#             for l in range(4):
#                 ddx = dx[l] + xx
#                 ddy = dy[l] + yy
#                 ddz = dz[k] + zz
#
#                 if 0 <= ddx < m and 0 <= ddy < n and 0 <= ddz < k:
#                     if graph[ddx][ddy][ddz] == 0:
#                         graph[ddx][ddy][ddz] = graph[xx][yy][zz] + 1
#                         cnt = max(cnt, graph[ddx][ddy][ddz])
#                         q.append((ddx, ddy, ddz))
#
#
# bfs()
# for i in range(k):
#     for j in range(n):
#         for k in range(m):
#             if graph[k][j][i] == -1:
#                 print(-1)
#                 sys.exit()
# print(cnt)
