import sys
from collections import deque
n = int(sys.stdin.readline())
graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

li = []
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    graph.append(tmp)

    for i in tmp:
        if i not in li:
            li.append(i)


def bfs(xx, yy, value):
    q = deque()
    q.append((xx, yy))
    visited[xx][yy] = True

    while q:
        x, y = q.popleft()
        for k in range(4):
            ddx = dx[k] + x
            ddy = dy[k] + y
            if 0 <= ddx < n and 0 <= ddy < n:
                if not visited[ddx][ddy] and graph[ddx][ddy] >= value:
                    visited[ddx][ddy] = True
                    q.append((ddx, ddy))


result = []
for t in li:
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] >= t:
                bfs(i, j, t)
                cnt += 1
    result.append(cnt)

print(max(result))

