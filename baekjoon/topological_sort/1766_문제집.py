import sys
import heapq
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
degree = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    degree[b] += 1
    graph[a].append(b)

q = []
heapq.heapify(q)
for i in range(1, n+1):
    if degree[i] == 0:
        heapq.heappush(q, (1, i))

res = []
while q:
    pri, now = heapq.heappop(q)
    res.append(now)
    for i in graph[now]:
        degree[i] -= 1
        if degree[i] == 0:
            heapq.heappush(q, (0, i))
print(*res)