import sys

n = int(sys.stdin.readline())
sys.setrecursionlimit(10 ** 6)
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def dfs(x, y):
    if visited[x][y] < 0:
        visited[x][y] = 0
        for k in range(4):
            ddx = x + dx[k]
            ddy = y + dy[k]
            if 0 <= ddx < n and 0 <= ddy < n:
                if graph[x][y] < graph[ddx][ddy]:
                    visited[x][y] = max(visited[x][y], dfs(ddx, ddy))
        visited[x][y] += 1
    return visited[x][y]


visited = [[-1] * n for _ in range(n)]
result = 0
for i in range(n):
    for j in range(n):
        result = max(result, dfs(i, j))

print(result)



# bfs 시간초과
# def bfs(x, y):
#     q = deque()
#     q.append((x, y))
#     visited[x][y] = 1
#
#     while q:
#         xx, yy = q.popleft()
#         for k in range(4):
#             ddx = xx + dx[k]
#             ddy = yy + dy[k]
#             if 0 <= ddx < n and 0 <= ddy < n:
#                 if visited[ddx][ddy] == -1 and graph[xx][yy] < graph[ddx][ddy]:
#                     visited[ddx][ddy] = visited[xx][yy] + 1
#                     q.append((ddx, ddy))
#
#
#
# result = 0
# for i in range(n):
#     for j in range(n):
#         visited = [[-1] * (n + 1) for _ in range(n)]
#         bfs(i, j)
#         for v in visited:
#             result = max(result, max(v))
#
# print(result)
