import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

q = deque([(0, 0, 1)])
visited[0][0][1] = 1

while q:
    x, y, z = q.popleft()
    if x == n - 1 and y == m - 1:
        print(visited[x][y][z])
        sys.exit(0)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1 and z == 1 and visited[nx][ny][0] == 0:
                visited[nx][ny][0] = visited[x][y][z] + 1
                q.append((nx, ny, 0))
            elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                q.append((nx, ny, z))
print(-1)

# 얘는 01bfs안됨
# 가중치가 0인간선이 없어서
