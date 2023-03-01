import sys
from collections import deque
n = int(sys.stdin.readline())
r1, c1, r2, c2 = map(int, sys.stdin.readline().split())

visited = [[-1] * n for _ in range(n)]
d = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 0

    while q:
        xx, yy = q.popleft()
        if xx == r2 and yy == c2:

            break
        for dx, dy in d:
            ddx = xx + dx
            ddy = yy + dy
            if 0 <= ddx < n and 0 <= ddy < n:
                if visited[ddx][ddy] == -1:
                    visited[ddx][ddy] = visited[xx][yy] + 1
                    q.append((ddx, ddy))



bfs(r1, c1)

print(visited[r2][c2])