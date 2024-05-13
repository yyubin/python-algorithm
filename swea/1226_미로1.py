from collections import deque

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        xx, yy = q.popleft()
        for k in range(4):
            ddx = xx + dx[k]
            ddy = yy + dy[k]

            if 0 <= ddx < 16 and 0 <= ddy < 16 and not visited[ddx][ddy]:
                visited[ddx][ddy] = True
                if graph[ddx][ddy] == 3:
                    return True
                elif graph[ddx][ddy] == 0:
                    q.append((ddx, ddy))


for tc in range(1, 11):
    _ = int(input())
    graph = [list(map(int, input())) for _ in range(16)]
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    visited = [[False] * 16 for _ in range(16)]
    result = 0

    for i in range(16):
        for j in range(16):
            if graph[i][j] == 2:
                if bfs(i, j):
                    result = 1
                    break

    print(f'#{tc} {result}')
