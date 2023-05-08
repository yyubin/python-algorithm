import sys
from collections import deque
r, c = map(int, sys.stdin.readline().split())
graph = []
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

jh = ()

for i in range(r):
    li = list(sys.stdin.readline().rstrip())
    graph.append(li)
    for j, v in enumerate(li):
        if v == 'J':
            jh = ('J', i, j)

q = deque()
visited = [[0] * r for _ in range(c)]

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'F':
            q.append(('F', i, j))

q.append(jh)

while q:
    done = False
    s, x, y = q.popleft()
    if x == 0 or y == 0 or x == c-1 or y == r-1:
        print(visited[x][y] + 1)
        break
    for i in range(4):
        ddx = x + dx[i]
        ddy = y + dy[i]
        if 0 <= ddx < c and 0 <= ddy < r:
            if s == 'J' and graph[ddx][ddy] == '.' and visited[ddx][ddy] == 0:
                graph[x][y] = '.'
                visited[ddx][ddy] = visited[x][y] + 1
                q.append(('J', ddx, ddy))
            elif s == 'F' and graph[ddx][ddy] != '#':
                if graph[ddx][ddy] == 'J':
                    done = True
                    break
                else:
                    graph[ddx][ddy] = 'F'

    if done:
        print("IMPOSSIBLE")
        break




