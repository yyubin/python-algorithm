import sys
from collections import deque
n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def bfs(start, end):
    q = deque()
    q.append([start, 0])
    visited[start] = True
    ans = 0

    while q:
        now, val = q.popleft()
        ans = max(ans, val)

        for v, c in graph[now]:
            if not visited[v]:
                visited[v] = True
                q.append([v, c+val])

    return ans

visited = [False] * (n + 1)
print(bfs(1, n))

