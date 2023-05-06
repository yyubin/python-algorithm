from collections import deque
n, k = map(int, input().split())
graph = []
data = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], i, j, 0))

rs, rx, ry = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

data.sort()
q = deque(data)

while q:
    virus, x, y, time = q.popleft()
    if time == rs:
        break
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if 0 <= mx < n and 0 <= my < n:
            if graph[mx][my] == 0:
                graph[mx][my] = virus
                q.append((virus, mx, my, time+1))

print(graph[rx - 1][ry - 1])

## 위는 맞고 아래는 틀림
# 같은 로직인데 왜 그런지 못 찾겠음..
import sys
from collections import deque
graph = []
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
n, k = map(int, sys.stdin.readline().split())

virus = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], i, j, 0))

s, x, y = map(int, sys.stdin.readline().split())

virus.sort() ## sort 할때 graph[i][j] 기준으로 해줘야함
q = deque(virus)

while q:
    a, xx, yy, prev_s = q.popleft()
    if prev_s == s:
        break
    for k in range(4):
        nx = xx + dx[k]
        ny = yy + dy[k]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
            graph[nx][ny] = a
            q.append((a, nx, ny, prev_s + 1))

print(graph[x-1][y-1])




