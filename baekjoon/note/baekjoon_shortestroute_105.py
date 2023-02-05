#1753번 : 최단경로
import heapq
n, m = map(int, input().split())
start = int(input())
INF = int(1e9)

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

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


dijkstra(start)

for i in range(1, len(distance)):
    if distance[i] == 1e9:
        print("INF")
    else:
        print(distance[i])
print(distance[i] if distance[i] != 1e9 else "INF" for i in range(1, len(distance)))

# 1916번 : 최소비용 구하기
# import heapq
# INF = int(1e9)
#
# n = int(input())
# m = int(input())
#
# graph = [[] for i in range(n+1)]
# distance = [INF] * (n+1)
#
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))
#
# start, end = map(int, input().split())
#
#
# def dijkstra(start):
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
#
# dijkstra(start)
#
# print(distance[end])

# 11779번 : 최소비용 구하기 2
# import heapq
# INF = int(1e9)
#
# n = int(input())
# m = int(input())
#
# graph = [[] for i in range(n+1)]
# distance = [INF] * (n+1)
#
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))
#
# start, end = map(int, input().split())
#
# result = []
#
# def dijkstra(start):
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
#                 result.append((i, i[1]))
#                 heapq.heappush(q, (cost, i[0]))
#
#
# dijkstra(start)
#
#
#
# print(distance[end])
# print(result)
# print(graph)

# 5972번 : 택배배송
# import heapq
# INF = int(1e9)
#
# n, m = map(int, input().split())
#
# graph = [[] for i in range(n+1)]
# distance = [INF] * (n+1)
#
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))
#     graph[b].append((a, c))
#
#
# def dijkstra(start):
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
#
# dijkstra(1)
#
# print(distance[n])