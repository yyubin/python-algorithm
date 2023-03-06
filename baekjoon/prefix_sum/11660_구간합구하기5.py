import sys
n, m = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

d = [[0] * (n+1) for _ in range(n+1)]

_sum = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        d[i][j] = d[i][j-1] + d[i-1][j] - d[i-1][j-1] + graph[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(d[x2][y2] - d[x2][y1-1] - d[x1-1][y2] + d[x1-1][y1-1])

