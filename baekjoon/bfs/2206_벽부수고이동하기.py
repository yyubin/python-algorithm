import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs():
    q = deque()
    q.append((0, 0, 1))
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1

    while q:
        a, b, c = q.popleft()
        if a == n-1 and b == m-1:
            return visited[a][b][c]
        for k in range(4):
            ddx = dx[k] + a
            ddy = dy[k] + b
            if 0 <= ddx < n and 0 <= ddy < m:
                if graph[ddx][ddy] == 1 and c == 1:
                    visited[ddx][ddy][0] = visited[a][b][c] + 1
                    q.append((ddx, ddy, 0))
                elif graph[ddx][ddy] == 0 and visited[ddx][ddy][c] == 0:
                    visited[ddx][ddy][c] = visited[a][b][c] + 1
                    q.append((ddx, ddy, c))
    return -1

print(bfs())
