import sys
from collections import deque
graph = []
for _ in range(12):
    graph.append(list(sys.stdin.readline().rstrip()))

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(color, x, y):
    q = deque()
    visited = [[-1] * 6 for _ in range(12)]
    q.append((x, y))
    visited[x][y] = 0
    result = [(x, y)]

    while q:
        xx, yy = q.popleft()
        for k in range(4):
            ddx = xx + dx[k]
            ddy = yy + dy[k]
            if 0 <= ddx < 12 and 0 <= ddy < 6:
                if graph[ddx][ddy] == color and visited[ddx][ddy] == -1:
                    q.append((ddx, ddy))
                    result.append((ddx, ddy))
                    visited[ddx][ddy] = 0

    return result

def gravity():
    for n in range(6):
        q = deque()
        for m in range(12):
            if graph[m][n] != '.':
                q.append(graph[m][n])
                graph[m][n] = '.'

        idx = 11
        while q:
            graph[idx][n] = q.popleft()
            idx -= 1


cnt = 0
for i in range(12):
    for j in range(6):
        if graph[i][j] != '.':
            li = bfs(graph[i][j], i, j)
            if len(li) >= 4:
                for a, b in li:
                    graph[a][b] = '.'
                gravity()
                cnt += 1

print(cnt)
