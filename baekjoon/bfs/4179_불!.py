import sys
from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
def bfs(l, x, y):
    done = False
    q = deque()
    visited[x][y] = 1
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 'F':
                q.append(('F', i, j))
                visited[i][j] = True
    q.append((l, x, y))

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
                if ll == 'J':
                    print(visited[xx][yy])
                    done = True
                    break
        if done:
            break
    else:
        print("IMPOSSIBLE")


h, w = map(int, sys.stdin.readline().split())
graph = []
visited = [[-1] * w for _ in range(h)]

for _ in range(h):
    graph.append(list(sys.stdin.readline()))

for i in range(h):
    for j in range(w):
        if graph[i][j] == 'J':
            bfs('J', i, j)
