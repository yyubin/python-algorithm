import heapq
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

q = []
heapq.heappush(q, (0, 1))

ans = 0

while q:
    w, dest = heapq.heappop(q)
    if not visited[dest]:
        visited[dest] = True
        ans += w
        for next_wei, next_node in graph[dest]:
            heapq.heappush(q, (next_wei, next_node))

print(ans)


