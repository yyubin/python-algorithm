import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

result = []

def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    cnt = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            ddx = x + dx[i]
            ddy = y + dy[i]
            if 0 <= ddx < n and 0 <= ddy < m and not visited[ddx][ddy]:
                if graph[ddx][ddy] == 0:
                    visited[ddx][ddy] = True
                    q.append((ddx, ddy))
                elif graph[ddx][ddy] == 1:
                    graph[ddx][ddy] = 0
                    visited[ddx][ddy] = True
                    cnt += 1


    result.append(cnt)
    return cnt

t = 0

while True:
    t += 1
    visited = [[False] * m for _ in range(n)]
    cnt = bfs()

    if cnt == 0:
        break

print(t-1)
print(result[-2])