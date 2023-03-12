import sys
from collections import deque

t = int(sys.stdin.readline())
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def bfs(l, x, y):
    done = False
    q = deque()
    visited[x][y] = 1
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '*':
                q.append(('*', i, j))
                visited[i][j] = True
    q.append((l, x, y))
    ## 불이 먼저 큐에 들어가야함
    # 불이 이동할 경로에 상근이가 있으면 IMPOSSIBLE

    while q:
        ll, xx, yy = q.popleft()
        for k in range(4):
            ddx = xx + dx[k]
            ddy = yy + dy[k]
            if 0 <= ddx < h and 0 <= ddy < w:
                if visited[ddx][ddy] == -1 and graph[ddx][ddy] == '.':
                    q.append((ll, ddx, ddy))
                    visited[ddx][ddy] = visited[xx][yy] + 1
            else:
                if ll == '@':
                    print(visited[xx][yy])
                    done = True
                    break
        if done:
            break
    else:
        print("IMPOSSIBLE")


for _ in range(t):
    w, h = map(int, sys.stdin.readline().split())
    graph = []
    visited = [[-1] * w for _ in range(h)]

    for _ in range(h):
        graph.append(list(sys.stdin.readline()))

    for i in range(h):
        for j in range(w):
            if graph[i][j] == '@':
                bfs('@', i, j)
