import sys
from collections import deque

n = int(sys.stdin.readline())
graph = []

for _ in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, color):
    q = deque()
    q.append((x, y))

    while q:
        a, b = q.popleft()
        for k in range(4):
            ddx = dx[k] + a
            ddy = dy[k] + b
            if 0 <= ddx < n and 0 <= ddy < n:
                if not visited[ddx][ddy] and color == graph[ddx][ddy]:
                    q.append((ddx, ddy))
                    visited[ddx][ddy] = True


visited = [[False] * n for _ in range(n)]
cnt1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, graph[i][j])
            cnt1 += 1


visited = [[False] * n for _ in range(n)]
cnt2 = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, graph[i][j])
            cnt2 += 1

print(cnt1, end=" ")
print(cnt2)
