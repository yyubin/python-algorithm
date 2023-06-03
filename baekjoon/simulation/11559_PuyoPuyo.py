import sys
from collections import deque

graph = []
for _ in range(12):
    graph.append(list(sys.stdin.readline().rstrip()))

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        xx, yy = q.popleft()
        for k in range(4):
            ddx = xx + dx[k]
            ddy = yy + dy[k]
            if 0 <= ddx < 12 and 0 <= ddy < 6:
                if graph[ddx][ddy] == graph[xx][yy] and visited[ddx][ddy] == -1:
                    q.append((ddx, ddy))
                    result.append((ddx, ddy))
                    visited[ddx][ddy] = 0


def delete(result):
    for a, b in result:
        graph[a][b] = '.'


def gravity():
    for n in range(6):
        for m in range(10, -1, -1):
            for k in range(11, m, -1):
                if graph[m][n] != '.' and graph[k][n] == '.':
                    graph[k][n] = graph[m][n]
                    graph[m][n] = '.'
                    break


cnt = 0

while True:
    flag = 0
    visited = [[-1] * 6 for _ in range(12)]

    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.' and visited[i][j] == -1:
                visited[i][j] = 0
                result = [(i, j)]
                bfs(i, j)
                if len(result) >= 4:
                    flag = 1
                    delete(result)

    if flag == 0:
        break
    gravity()
    cnt += 1

print(cnt)
