import sys
sys.setrecursionlimit(10 ** 8)
m, n = map(int, sys.stdin.readline().split())
graph = []

for _ in range(m):
    graph.append(list(map(int, sys.stdin.readline().split())))

visited = [[-1 for _ in range(n)] for _ in range(m)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
def dfs(x, y):
    if x == (m-1) and y == (n-1):
        return 1

    if visited[x][y] == -1:
        visited[x][y] = 0

        for k in range(4):
            ddx = x + dx[k]
            ddy = y + dy[k]
            if 0 <= ddx < m and 0 <= ddy < n:
                if graph[x][y] > graph[ddx][ddy]:
                    visited[x][y] += dfs(ddx, ddy)

    return visited[x][y]


print(dfs(0, 0))

