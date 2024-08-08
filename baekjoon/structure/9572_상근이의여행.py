import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]
    q = deque()
    visited = [False] * (n+1)
    cnt = 0

    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())

        graph[a].append(b)
        graph[b].append(a)

        if i == 0:
            q.append(a)
            visited[a] = True

    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                cnt += 1

    print(cnt)
