import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[1e9] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = min(c, graph[a-1][b-1])

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in graph:
    for j in i:
        print(j if j != 1e9 else 0, end=" ")
    print()


# 다익스트라 시간초과

# import sys
# import heapq
# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())
# INF = int(1e9)
#
# graph = [[] for _ in range(n + 1)]
#
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))
#
# def dijkstra(start, end):
#     distance = [INF] * (n + 1)
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#
#     while q:
#         dist, now = heapq.heappop(q)
#
#         if distance[now] < dist:
#             continue
#
#         for i in graph[now]:
#             cost = dist + i[1]
#
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
#
#     return distance[end]
#
# result = [[0] * (n+1) for _ in range(n+1)]
#
# for i in range(1, len(graph)):
#     for j in range(1, len(graph)):
#         result[i][j] = dijkstra(i, j)
#
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(result[i][j], end=" ")
#     print()
#
