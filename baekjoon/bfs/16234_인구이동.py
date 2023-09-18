import sys
from collections import deque

graph = []
n, l, r = map(int, sys.stdin.readline().split())

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(x, y):
    q = deque()
    tmp = []
    q.append((x, y))
    tmp.append((x, y))

    while q:
        xx, yy = q.popleft()

        for k in range(4):
            ddx = xx + dx[k]
            ddy = yy + dy[k]

            if 0 <= ddx < n and 0 <= ddy < n and visited[ddx][ddy] == 0:
                if l <= abs(graph[ddx][ddy] - graph[xx][yy]) <= r:
                    visited[ddx][ddy] = 1
                    q.append((ddx, ddy))
                    tmp.append((ddx, ddy))

    return tmp


result = 0

while True:
    visited = [[0] * (n+1) for _ in range(n+1)]
    flag = 0

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                area = bfs(i, j)

                if len(area) > 1:
                    flag = 1
                    val = sum([graph[x][y] for x, y in area]) // len(area)

                    for x, y in area:
                        graph[x][y] = val

    if flag == 0:
        break

    result += 1

print(result)


# import sys
# from collections import deque
# import math
#
# n, l, r = map(int, sys.stdin.readline().split())
# graph = [] * n
# check = [False * n for _ in range(n)]
# dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
#
# for _ in range(n):
#     tmp = list(map(int, sys.stdin.readline().split()))
#     tmp2 = []
#     for i in tmp:
#         tmp2.append([i] + [False])
#
#     graph.append(tmp2)
#
#
# def bfs(x, y, cnt, sum_):
#     q = deque()
#     q.append((x, y))
#     flag = False
#
#     while q:
#         xx, yy = q.popleft()
#
#         for k in range(4):
#             ddx = xx + dx[k]
#             ddy = yy + dy[k]
#             if 0 <= ddx < n and 0 <= ddy < n and not graph[ddx][ddy][1]:
#                 if l <= abs(graph[ddx][ddy][0] - graph[x][y][0]) <= r:
#                     graph[ddx][ddy][1] = True
#                     q.append((ddx, ddy))
#                     cnt += 1
#                     sum_ += graph[ddx][ddy][0]
#
#                     if not flag:
#                         graph[xx][yy][1] = True
#                         cnt += 1
#                         sum_ += graph[xx][yy][0]
#                         flag = True
#
#     return cnt, sum_
#
#
# def change(cnt, sum_):
#     val = math.trunc(sum_ / cnt)
#     for i in range(n):
#         for j in range(n):
#             if graph[i][j][1]:
#                 graph[i][j][0] = val
#                 graph[i][j][1] = False
#
#     print(graph)
#     print(val)
#
# cnt, sum_ = 0, 0
# result = 0
#
# ## 이쪽 for 문을 다시 설계해야함
# # result가 걸린 날이 아닌 연합국 수를 배출함
# for i in range(n):
#     for j in range(n):
#         if not graph[i][j][1]:
#             nxt_cnt, nxt_sum = bfs(i, j, cnt, sum_)
#             if nxt_cnt != cnt:
#                 cnt = nxt_cnt
#                 sum_ = nxt_sum
#                 result += 1
#                 change(cnt, sum_)
#
# print(result)
