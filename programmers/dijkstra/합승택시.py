import heapq

INF = 1e9

def dijkstra(graph, n, start):
    distance = [INF for _ in range(n + 1)]
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist + i[1], i[0]))
    return distance

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]

    for u, v, w in fares:
        graph[u].append((v, w))
        graph[v].append((u, w))

    s_dist = dijkstra(graph, n, s)
    a_dist = dijkstra(graph, n, a)
    b_dist = dijkstra(graph, n, b)

    answer = INF
    for i in range(1, n + 1):
        answer = min(answer, s_dist[i] + a_dist[i] + b_dist[i])

    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))


## 바로 갈라지지 않으려면 분기 될 지점 골라서 3방향 값 더해준 것 중 최소 골라야 함