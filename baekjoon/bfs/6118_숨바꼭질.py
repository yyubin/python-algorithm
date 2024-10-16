import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
nodes = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    nodes[a].append(b)
    nodes[b].append(a)

visited = [sys.maxsize] * (n+1)

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 0

    while q:
        now = q.popleft()
        for next in nodes[now]:
            if visited[now] + 1 < visited[next]:
                visited[next] = visited[now] + 1
                q.append(next)


bfs(1)
visited.pop(0)

result_node = 0
result_dist = 0
tmp = 0
for i in range(n):
    if tmp < visited[i]:
        result_node = i
        result_dist = visited[i]
        tmp = result_dist

print(result_node+1, result_dist, visited.count(result_dist))
