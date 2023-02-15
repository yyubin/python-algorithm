# import copy
# import sys
# n, m = map(int, sys.stdin.readline().split())
# graph = []
# visited = [[False] * m for _ in range(n)]
#
# for _ in range(n):
#     graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
#
# def dfs(x, y, dx, dy, tmp_graph):
#     visited[x][y] = True
#     for k in range(len(dx)):
#         ddx = dx[k] + x
#         ddy = dy[k] + y
#         if 0 <= ddx < m and 0 <= ddy < n:
#             if tmp_graph[ddx][ddy] == 0 and not visited[x][y]:
#                 tmp_graph[ddx][ddy] = '#'
#                 dfs(ddx, ddy, dx, dy, tmp_graph)
#
# def count(tmp_graph):
#     global result
#     cnt = 0
#     for a in range(n):
#         for b in range(m):
#             if tmp_graph[a][b] == 0:
#                 cnt += 1
#     result = max(cnt, result)
#
#
# result = 0
#
# for x in range(n):
#     for y in range(m):
#         dx = [1, -1, 0, 0]
#         dy = [0, 0, 1, -1]
#         if graph[x][y] == 1:
#             for k in range(len(dx)):
#                 tmp_graph = copy.deepcopy(graph)
#                 dfs(x, y, dx, dy, tmp_graph)
#                 count(tmp_graph)
#         elif graph[x][y] == 2:
#             dx = [[1, -1], [0, 0]]
#             dy = [[0, 0], [1, -1]]
#             for i in range(2):
#                 tmp_graph = copy.deepcopy(graph)
#                 dfs(x, y, dx, dy, tmp_graph)
#                 count(tmp_graph)
#         elif graph[x][y] == 3:
#             dx = [[1, 0], [1, 0], [-1, 0], [-1, 0]]
#             dy = [[0, 1], [0, -1], [0, 1], [0, -1]]
#             for i in range(4):
#                 tmp_graph = copy.deepcopy(graph)
#                 dfs(x, y, dx[i], dy[i], tmp_graph)
#                 count(tmp_graph)
#         elif graph[x][y] == 4:
#             dx = [[1, -1, 0], [1, 0, 0], [1, 0, -1], [-1, 1, 0]]
#             dy = [[0, 0, 1], [0, 1, -1], [0, -1, 0], [0, 0, -1]]
#             for i in range(4):
#                 tmp_graph = copy.deepcopy(graph)
#                 dfs(x, y, dx[i], dy[i], tmp_graph)
#                 count(tmp_graph)
#         elif graph[x][y] == 5:
#             tmp_graph = copy.deepcopy(graph)
#             dfs(x, y, dx, dy, tmp_graph)
#             count(tmp_graph)
#
# print(result)
import copy
import sys
n, m = map(int, sys.stdin.readline().split())
cctv = []
graph = []
min_value = int(1e9)

mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    graph.append(data)
    for j in range(m):
        if data[j] in [1, 2, 3, 4, 5]:
            cctv.append([data[j], i, j])

def fill(graph, mode, x, y):
    for i in mode:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if graph[nx][ny] == 6:
                break
            elif graph[nx][ny] == 0:
                graph[nx][ny] = -1

def dfs(depth, graph):
    global min_value
    if depth == len(cctv):
        count = 0
        for i in range(n):
            count += graph[i].count(0)
        min_value = min(min_value, count)
        return

    temp = copy.deepcopy(graph)
    cctv_num, x, y = cctv[depth]
    for i in mode[cctv_num]:
        fill(temp, i, x, y)
        dfs(depth+1, temp)
        temp = copy.deepcopy(graph)


dfs(0, graph)
print(min_value)

