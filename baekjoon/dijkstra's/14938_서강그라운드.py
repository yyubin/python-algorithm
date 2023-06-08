import sys
import heapq

INF = int(1e9)
n, m, r = map(int, sys.stdin.readline().split())
t = list(map(int, sys.stdin.readline().split()))

graph = [[] for _ in range(n + 1)]

for _ in range(r):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


result = 0

for i in range(1, n+1):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, i))
    distance[i] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    tmp = 0
    for k, v in enumerate(distance):
        if v <= m:
            tmp += t[k-1]
    result = max(tmp, result)


print(result)
