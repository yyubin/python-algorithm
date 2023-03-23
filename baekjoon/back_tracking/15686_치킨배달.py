import sys
from itertools import combinations
n, m = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

result = sys.maxsize
home = []
chicken = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

for chi in combinations(chicken, m):
    tmp = 0
    for h in home:
        chi_len = 999
        for j in range(m):
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        tmp += chi_len
    result = min(result, tmp)

print(result)



# def bfs():
#     q = deque()
#     visited = [[-1] * (n + 1) for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if graph[i][j] == 1:
#                 q.append((i, j))
#                 visited[i][j] = 0
#
#     while q:
#         xx, yy = q.popleft()
#         for k in range(4):
#             ddx = xx + dx[k]
#             ddy = yy + dy[k]
#             if 0 <= ddx < n and 0 <= ddy < n and visited[ddx][ddy] == -1:
#                 if graph[ddx][ddy] == 0:
#                     visited[ddx][ddy] = visited[xx][yy] + 1
#                     q.append((ddx, ddy))
#                 elif graph[ddx][ddy] == 2:
#                     return visited[xx][yy] + 1
#
#
# result = []
# tmp = []
#
# for i in range(n):
#     for j in range(n):
#         if len(tmp) == m:
#             for u, v in tmp:
#                 graph[u][v] = 0
#             result.append(bfs())
#             for u, v in tmp:
#                 graph[u][v] = 2
#             tmp = []
#         if graph[i][j] == 2:
#             tmp.append((i, j))
#
