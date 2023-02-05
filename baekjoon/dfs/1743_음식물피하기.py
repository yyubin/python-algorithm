import sys
sys.setrecursionlimit(100000)
n, m, k = map(int, sys.stdin.readline().rstrip().split())
graph = []

for _ in range(n):
    graph.append([0 for _ in range(m)])

for _ in range(k):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a - 1][b - 1] = 1

result = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    cnt = 1
    for i in range(4):
        ddx = dx[i] + x
        ddy = dy[i] + y
        if 0 <= ddx < n and 0 <= ddy < m:
            if graph[ddx][ddy] == 1:
                graph[ddx][ddy] = 0
                cnt += dfs(ddx, ddy)
    return cnt


for j in range(n):
    for k in range(m):
        if graph[j][k] == 1:
            graph[j][k] = 0
            result.append(dfs(j, k))

print(max(result))
