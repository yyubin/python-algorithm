import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    i, j, v = map(int, sys.stdin.readline().split())
    graph[i].append((j, v))
    graph[j].append((i, v))

def bfs(start, goal):
    q = deque()
    q.append((start, 0))
    visited = [False] * (n+1)
    visited[start] = True

    while q:
        now, dist = q.popleft()

        if now == goal:
            return dist

        for i, j in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append((i, dist+j))


for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    print(bfs(x, y))


