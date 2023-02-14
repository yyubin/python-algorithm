# import copy
# import sys
# from collections import deque
# from itertools import combinations
#
# d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
#
# n, m = map(int, sys.stdin.readline().split())
# graph = []
#
# for _ in range(n):
#     graph.append(list(map(int, sys.stdin.readline().split())))
#
# def count(tmp_graph):
#     cnt = 0
#     for i in range(n):
#         for k in range(m):
#             if tmp_graph[i][k] == 0:
#                 cnt += 1
#     return cnt
#
# def bfs(x, y, tmp_graph):
#     queue = deque()
#     for i in range(n):
#         for k in range(m):
#             if tmp_graph[i][k] == 2:
#                 queue.append((i, k))
#
#     while queue:
#         r, c = queue.popleft()
#
#         for i in range(4):
#             dr = r + d[i][0]
#             dc = c + d[i][1]
#
#             if (0 <= dr < n) and (0 <= dc < m):
#                 if tmp_graph[dr][dc] == 0:
#                     tmp_graph[dr][dc] = 2
#                     queue.append((dr, dc))
#
#     return count(tmp_graph)
#
# ch = []
# for x in range(n):
#     for y in range(m):
#         if graph[x][y] == 0:
#             ch.append((x, y))
#
# result = []
# lis = combinations(ch, 3)
# for i in lis:
#     for j in i:
#         tmp_graph = copy.deepcopy(graph)
#         result.append(bfs(j[0], j[1], tmp_graph))
#
# print(max(result))
# import copy
# import sys
#
# n, m = map(int, sys.stdin.readline().split())
# graph = []
#
# for _ in range(n):
#     graph.append(list(map(int, sys.stdin.readline().split())))
#
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# result = 0
#
#
# def count(tmp_graph):
#     cnt = 0
#     for i in range(n):
#         for k in range(m):
#             if tmp_graph[i][k] == 0:
#                 cnt += 1
#     return cnt
#
#
# def virus_dfs(x, y, tmp_graph):
#     for i in range(4):
#         ddx = x + dx[i]
#         ddy = y + dy[i]
#
#         if 0 <= ddx < m and 0 <= ddy < n:
#             if tmp_graph[ddx][ddy] == 0:
#                 tmp_graph[ddx][ddy] = 2
#                 virus_dfs(ddx, ddy)
#
#
# def dfs(count):
#     global result
#     if count == 3:
#         tmp_graph = copy.deepcopy(graph)
#         for i in range(n):
#             for j in range(m):
#                 if graph[i][j] == 2:
#                     virus_dfs(i, j, tmp_graph)
#             result = max(result, count(tmp_graph))
#             return
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 0:
#                 graph[i][j] = 1
#                 count += 1
#                 dfs(count)
#                 graph[i][j] = 0
#                 count -= 1
#
#
# dfs(0)
# print(result)


import sys, copy
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

max_result = 0

def virus():
    global max_result
    temp = copy.deepcopy(graph)
    result = 0
    q = deque()
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    q.append((nx, ny))
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                result += 1

    max_result = max(max_result, result)


def dfs(cnt):
    if cnt == 3:
        virus()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                dfs(cnt + 1)
                graph[i][j] = 0


dfs(0)
print(max_result)
