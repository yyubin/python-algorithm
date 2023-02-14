import sys
sys.setrecursionlimit(10**6)

r, c = map(int, sys.stdin.readline().split())
graph = []
visited = [[False] * c for _ in range(r)]
for _ in range(r):
    graph.append(list(sys.stdin.readline().rstrip()))

sheep = 0
wolf = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    global tmp_sheep
    global tmp_wolf
    visited[x][y] = True
    for k in range(4):
        ddx = dx[k] + x
        ddy = dy[k] + y
        if 0 <= ddx < r and 0 <= ddy < c:
            if graph[ddx][ddy] != '#' and not visited[ddx][ddy]:
                if graph[ddx][ddy] == 'o':
                    tmp_sheep += 1
                if graph[ddx][ddy] == 'v':
                    tmp_wolf += 1
                dfs(ddx, ddy)


for i in range(r):
    for j in range(c):
        tmp_sheep, tmp_wolf = 0, 0
        dfs(i, j)
        if tmp_sheep > tmp_wolf:
            sheep += tmp_sheep
        else:
            wolf += tmp_wolf

print(sheep, wolf)
