import sys
from collections import deque
n, m, p = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))

player = []
graph = []
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
for _ in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))

for i in range(n):
    for j in range(m):
        if graph[i][j] != '.' and graph[i][j] != '#':
            player.append((graph[i][j], i, j))


def bfs(x, y, play):
    q = deque()
    q.append((x, y))
    print("bfs시작")

    while q:
        xx, yy = q.popleft()
        for u in range(1, s[int(play)-1] + 1):
            for k in range(4):
                ddx = xx + dx[k] * u
                ddy = yy + dy[k] * u
                print(ddx, ddy)
                if 0 <= ddx < m and 0 <= ddy < n and graph[ddx][ddy] == '.':
                    graph[ddx][ddy] = play


while True:
    print(graph, sep="\n")
    flag = False
    for i in range(n):
        for j in range(m):
            if graph[i][j] != '.':
                flag = True


    if not flag:
        break

result = [0 for _ in range(p)]
for i in graph:
    for j in i:
        result[int(j)-1] += 1

print(*result, sep=" ")


