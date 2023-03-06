import sys
from collections import deque

t = int(sys.stdin.readline())
d = [(-1, 2), (-2, 1), (-1, -2), (-2, -1), (1, -2), (2, -1), (1, 2), (2, 1)]


def bfs(x, y, to_x, to_y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        xx, yy = q.popleft()
        if xx == to_x and yy == to_y:
            print(visited[to_x][to_y] - 1)
            break
        for dx, dy in d:
            ddx = xx + dx
            ddy = yy + dy
            if 0 <= ddx < l and 0 <= ddy < l:
                if visited[ddx][ddy] == -1:
                    visited[ddx][ddy] = visited[xx][yy] + 1
                    q.append((ddx, ddy))



for _ in range(t):
    l = int(sys.stdin.readline())
    graph = [[0] * (l + 1) for _ in range(l + 1)]
    visited = [[-1] * (l + 1) for _ in range(l + 1)]

    now_x, now_y = map(int, sys.stdin.readline().split())
    to_x, to_y = map(int, sys.stdin.readline().split())
    bfs(now_x, now_y, to_x, to_y)
