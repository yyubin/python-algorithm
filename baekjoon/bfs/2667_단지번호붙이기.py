import sys
from collections import deque
n = int(sys.stdin.readline())
graph = []
visited = [[False] * n for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(a, b):
    q = deque()
    q.append((a, b))
    visited[a][b] = True
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            ddx = dx[i] + x
            ddy = dy[i] + y
            if 0 <= ddx < n and 0 <= ddy < n:
                if not visited[ddx][ddy] and graph[ddx][ddy] == 1:
                    visited[ddx][ddy] = True
                    q.append((ddx, ddy))
                    cnt += 1

    result.append(cnt)


result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            bfs(i, j)

print(len(result))
result.sort()
print(*result, sep="\n")
