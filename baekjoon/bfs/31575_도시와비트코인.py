import sys
from collections import deque
m, n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx, dy = [1, 0], [0, 1]
visited = [[False] * m for _ in range(n)]

def bfs():
    q = deque()
    q.append((0, 0))

    while q:
        x, y = q.popleft()
        if x == n-1 and y == m-1:
            return True
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny))

    return False

print("Yes" if bfs() else "No")


# YES가 아니라 Yes