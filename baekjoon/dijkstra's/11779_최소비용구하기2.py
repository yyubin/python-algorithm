import heapq

n = int(input())
m = int(input())
INF = int(1e9)

graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

s, t = map(int, input().split())

parent = [0 for i in range(0, n+1)]
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                parent[i[0]] = now


dijkstra(s)
print(distance[t])
result = [t]

while True:
    idx = parent[t]
    result.append(idx)
    if idx == s:
        break
    parent[t] = parent[parent[t]]

print(len(result))
print(*result[::-1])