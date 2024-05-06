import sys

n, m, k = map(int, sys.stdin.readline().split())
graph = [[0] * m for _ in range(n)]

def find_path(stx, sty, x, y):
    for i in range(stx, x):
        for j in range(sty, y):
            if i == stx or j == sty:
                graph[stx][sty] = 1
            graph[i][j] = graph[i - 1][j] + graph[i][j - 1]

    return graph[x-1][y-1]

if k == 0:
    print(find_path(0, 0, n, m))
else:
    mid_x = (k-1) // m
    mid_y = (k-1) % m

    print(find_path(0, 0, mid_x + 1, mid_y + 1) * find_path(mid_x, mid_y, n, m))

# import sys
# import math
# n, m, k = map(int, sys.stdin.readline().split())
# graph = [[0] * m for _ in range(n)]
# val = 1
# kx, ky = 0, 0
#
# for i in range(n):
#     for j in range(m):
#         graph[i][j] = val
#         if val == k:
#             kx, ky = i, j
#         val += 1
#
#
# if k == 0:
#     print(math.factorial(n+m)//math.factorial(n)*math.factorial(m))
#     sys.exit()
#
# tmp_x, tmp_y = kx-m, ky-n
# reach_x, reach_y = m-kx, n-ky
#
# tmp_path = math.factorial(tmp_x+tmp_x)//math.factorial(tmp_x)*math.factorial(tmp_y)
# reach_path = math.factorial(reach_x+reach_y)//math.factorial(reach_x)*math.factorial(reach_y)
#
# print(tmp_path+reach_path)
#
#
# # bfs아니고 dp문제
# # import copy
# # import sys
# # from collections import deque
# # n, m, k = map(int, sys.stdin.readline().split())
# # graph = [[0] * m for _ in range(n)]
# # idx = 1
# #
# # for i in range(n):
# #     for j in range(m):
# #         graph[i][j] = idx
# #         idx += 1
# #
# # dx, dy = [1, 0], [0, 1]
# # visited = [[False] * m for _ in range(n)]
# # cnt = 0
# #
# # def bfs(x, y):
# #     global cnt
# #     q = deque()
# #     q.append((x, y, [graph[x][y]]))
# #     visited[x][y] = True
# #
# #     while q:
# #         xx, yy, path = q.popleft()
# #         for ii in range(2):
# #             ddx = dx[ii] + xx
# #             ddy = dy[ii] + yy
# #             if 0 <= ddx < n and 0 <= ddy < m:
# #                 visited[ddx][ddy] = True
# #                 tmp_path = copy.deepcopy(path)
# #                 tmp_path.append(graph[ddx][ddy])
# #                 if graph[ddx][ddy] == idx-1 and k != 0 and k in tmp_path:
# #                     cnt += 1
# #                 elif graph[ddx][ddy] == idx-1 and k == 0:
# #                     cnt += 1
# #                 else:
# #                     q.append((ddx, ddy, tmp_path))
# #
# # bfs(0, 0)
# #
# # print(cnt)
# #
# #
# #
# #
# #
