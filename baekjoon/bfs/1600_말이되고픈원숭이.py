import sys
from collections import deque

k = int(sys.stdin.readline())
w, h = map(int, sys.stdin.readline().split())
graph = []

for _ in range(h):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
horse_dx, horse_dy = [2, 1, 2, 1, -2, -2, -1, -1], [1, 2, -1, -2, 1, -1, 2, -2]

visited = [[[0] * (k + 1) for _ in range(w)] for _ in range(h)]


def bfs():
    global k
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1

    while q:
        x, y, z = q.popleft()
        if x == h - 1 and y == w - 1:
            return visited[x][y][z] - 1

        for i in range(4):
            ddx = dx[i] + x
            ddy = dy[i] + y
            if 0 <= ddx < h and 0 <= ddy < w and visited[ddx][ddy][z] == 0:
                if graph[ddx][ddy] == 0:
                    visited[ddx][ddy][z] = visited[x][y][z] + 1
                    q.append((ddx, ddy, z))
        if z < k:
            for i in range(8):
                ddx = horse_dx[i] + x
                ddy = horse_dy[i] + y
                if 0 <= ddx < h and 0 <= ddy < w and visited[ddx][ddy][z+1] == 0:
                    if graph[ddx][ddy] == 0:
                        visited[ddx][ddy][z+1] = visited[x][y][z] + 1
                        q.append((ddx, ddy, z+1))
    return -1


print(bfs())