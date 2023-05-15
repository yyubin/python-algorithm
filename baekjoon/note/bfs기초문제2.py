import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        now_x, now_y = q.popleft()
        if now_x == n - 1 and now_y == m - 1:
            print(graph[now_x][now_y])
            break

        for i in range(4):
            ddx = now_x + dx[i]
            ddy = now_y + dy[i]
            if 0 <= ddx < n and 0 <= ddy < m:
                if graph[ddx][ddy] == 1:
                    q.append((ddx, ddy))
                    graph[ddx][ddy] = graph[now_x][now_y] + 1


bfs(0, 0)
