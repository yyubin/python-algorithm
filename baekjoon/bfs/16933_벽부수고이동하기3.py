import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
graph = []

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

visited = [[k+1 for _ in range(m)] for _ in range(n)]

def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0] = 0
    time = True
    ans = 1

    while q:
        for _ in range(len(q)):
            x, y, cnt = q.popleft()
            if x == n - 1 and y == m - 1:
                print(ans)
                return
            for i in range(4):
                ddx = dx[i] + x
                ddy = dy[i] + y
                if 0 <= ddx < n and 0 <= ddy < m and visited[ddx][ddy] > cnt:
                    if graph[ddx][ddy] == 0:
                        visited[ddx][ddy] = cnt
                        q.append((ddx, ddy, cnt))
                    elif graph[ddx][ddy] == 1 and cnt < k:
                        if time:
                            visited[ddx][ddy] = cnt
                            q.append((ddx, ddy, cnt+1))
                        else:
                            q.append((x, y, cnt))
        time = not time
        ans += 1
    print(-1)

bfs()