import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = []
visited = [[False] * m for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

x, y = 0, 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
cnt = 0

def bfs(x, y):
    global cnt
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if x == n - 1 and y == m - 1:
                print(graph[n - 1][m - 1])
                break

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == False and graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    visited[nx][ny] = True
                    q.append([nx, ny])

bfs(0, 0)

### dfs는 최단 경로에 쓰이지 않는것 같아유
# def miro(x, y):
#     global cnt
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#     if graph[x][y] == 1:
#         cnt += 1
#         graph[x][y] = 0
#         if miro(x+1, y) or miro(x, y+1):
#             return True
#         elif miro(x-1, y) or miro(x, y-1):
#             return True
#     return False
#
#
# for i in range(m):
#     for j in range(n):
#         miro(i, j)
