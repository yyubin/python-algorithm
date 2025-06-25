import sys
from collections import deque
n, m, k = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [-1] * (n+1)

def bfs(start):
    q = deque([start])
    visited[start] = 0

    while q:
        now = q.popleft()
        for next in graph[now]:
            if visited[next] == -1:
                visited[next] = visited[now] + 1
                q.append(next)

bfs(k)
print(*visited[1:], sep='\n')