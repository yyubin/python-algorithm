from collections import deque
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        xx, yy = q.popleft()
        for k in range(4):
            ddx = xx + dx[k]
            ddy = yy + dy[k]
            if 0 <= ddx < 100 and 0 <= ddy < 100 and not visited[ddx][ddy]:
                visited[ddx][ddy] = True
                if graph[ddx][ddy] == 0:
                    q.append((ddx, ddy))
                elif graph[ddx][ddy] == 3:
                    return 1

    return 0

for _ in range(1, 11):
    t = int(input())
    graph = [list(map(int, input())) for _ in range(100)]
    visited = [[False] * 100 for _ in range(100)]
    result = 0

    for i in range(100):
        for j in range(100):
            if graph[i][j] == 2:
                result = bfs(i, j)

    print(f'#{t} {result}')
