import sys
n, m = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))

visited = [[False] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, cnt):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            return
        if graph[nx][ny] in ['#', 'F']:
            return
        elif graph[nx][ny] == '.' and not visited[nx][ny]:
            cnt += 1
            dfs(nx, ny, cnt)


def spread_fire():
    pass
