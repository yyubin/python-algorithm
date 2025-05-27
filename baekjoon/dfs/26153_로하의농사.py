import sys
sys.setrecursionlimit(10 ** 6)
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
now_x, now_y, p = map(int, sys.stdin.readline().split())
direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
max_water = 0
def dfs(x, y, dir, mat, visited, res):
    global max_water
    if mat > p:
        return
    max_water = max(max_water, res)
    visited[x][y] = True

    for i, (dx, dy) in enumerate(direction):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            cost = 1 if dir == i or dir == -1 or abs(i - dir) == 2 else 2
            if mat + cost <= p:
                visited[nx][ny] = True
                dfs(nx, ny, i, mat + cost, visited, res + graph[nx][ny])
                visited[nx][ny] = False

for k in range(4):
    visited = [[False]*m for _ in range(n)]
    visited[now_x][now_y] = True
    dfs(now_x, now_y, k, 0, visited, graph[now_x][now_y])

print(max_water)