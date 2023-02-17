import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(input().strip()) for _ in range(n)]

distance = [[0] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
queue = deque()


def bfs(Dx, Dy):
    while queue:
        x, y = queue.popleft()
        if graph[Dx][Dy] == 'S':
            return distance[Dx][Dy]
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if (graph[nx][ny] == '.' or graph[nx][ny] == 'D') and graph[x][y] == 'S':
                    graph[nx][ny] = 'S'
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))
                elif (graph[nx][ny] == '.' or graph[nx][ny] == 'S') and graph[x][y] == '*':
                    graph[nx][ny] = '*'
                    queue.append((nx, ny))

    return "KAKTUS"

for x in range(n):
    for y in range(m):
        if graph[x][y] == 'S': #고슴도치 위치부터 넣어주기
            queue.append((x, y))
        elif graph[x][y] == 'D':
            Dx, Dy = x, y

for x in range(n):
    for y in range(m):
        if graph[x][y] == '*': #물 위치 넣어주기 큐에는 항상 고슴도치 다음 물
            queue.append((x, y))

print(bfs(Dx, Dy))

