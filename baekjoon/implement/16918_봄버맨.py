import sys
from collections import deque
r, c, n = map(int, sys.stdin.readline().split())
graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(r)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
bomb = deque()

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'O':
            bomb.append((i, j))

time = 1

while time < n:
    for i in range(r):
        for j in range(c):
            if graph[i][j] == '.':
                graph[i][j] = 'O'

    time += 1

    if time == n:
        break

    while bomb:
        x, y = bomb.popleft()
        graph[x][y] = '.'
        for k in range(4):
            ddx = dx[k] + x
            ddy = dy[k] + y
            if 0 <= ddx < r and 0 <= ddy < c:
                graph[ddx][ddy] = '.'

    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'O':
                bomb.append((i, j))

    time += 1


for i in graph:
    print(*i, sep="")


