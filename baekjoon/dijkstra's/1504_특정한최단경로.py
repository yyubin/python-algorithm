import heapq

n, m = map(int, input().split())
INF = int(1e9)

# 각 노드에 연결되어 있는 노드에 대한 정를 담는 리스트 만들기
graph = [[] for i in range(n + 1)]  # range(n+1)은 노드의 개수\

for _ in range(m):  # 통로 정보 받기
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # a번 노드에서  b노드로 가는게 c만큼의 비용
    graph[b].append((a, c))

v1, v2 = map(int, input().split())


def dijkstra(start, end):
    distance = [INF] * (n + 1)
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

    return distance[end]


path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

result = min(path1, path2)

if result >= INF:
    print(-1)
else:
    print(result)
