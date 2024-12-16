import sys
n = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
result = [0, 0]

for i in range(n):
    r, c = 0, 0
    for j in range(n):
        if graph[i][j] == '.':
            r += 1
        else:
            r = 0
        if r == 2:
            result[0] += 1

        if graph[j][i] == '.':
            c += 1
        else:
            c = 0
        if c == 2:
            result[1] += 1

print(*result)


## 문제를 잘 읽자!!!!! ^^
# import sys
# from collections import deque
# n = int(sys.stdin.readline())
# graph = [list(map(str, sys.stdin.readline())) for _ in range(n)]
# dx_x, dy_x = [1, -1], [0, 0]
# dx_y, dy_y = [0, 0], [1, -1]
# visited = [[False] * n for _ in range(n)]
#
# res_x, res_y = 0, 0
#
# def bfs(x, y):
#     global res_x, res_y
#     q = deque()
#     q.append((x, y))
#     visited[x][y] = True
#
#     while q:
#         xx, yy = q.popleft()
#         for i in range(2):
#             ddx = xx + dx_x[i]
#             ddy = yy + dy_x[i]
#             if 0 <= ddx < n and 0 <= ddy < n and not visited[ddx][ddy] and graph[ddx][ddy] == ".":
#                 visited[ddx][ddy] = True
#
