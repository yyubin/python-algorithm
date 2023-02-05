# 전보
# import heapq
# n, m, start = map(int, input().split())
# INF = int(1e9) # 무한을 의미함
#
# # 각 노드에 연결되어 있는 노드에 대한 정를 담는 리스트 만들기
# graph = [[] for i in range(n+1)] # range(n+1)은 노드의 개수
# distance = [INF] * (n+1)
#
# for _ in range(m): #통로 정보 받기
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c)) # a번 노드에서  b노드로 가는게 c만큼의 비용
#
# def dijkstra(start):
#     q = []
#     # 시작노드로 가는 최단 경로는 0으로 해서 큐에 삽입
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#
#     while q:
#         # 비용과 현재 위치를 꺼냄
#         dist, now = heapq.heappop(q)
#
#         # distance는 무한대로 초기화했었음
#         # 만약 비용보다 작다면 이미 처리된 상태이고
#         # 처리가 되었어도 비용보다 작다면 넘어가야함
#         if distance[now] < dist:
#             continue
#
#         # 현재 위치의 그래프를 하나씩 순회,
#         for i in graph[now]:
#             cost = dist + i[1] # dist는 기존의 값, graph[now] 안에는 튜플이 (비용, 방향)으로 있음
#                                 # cost에 거쳐서 가는 값을 저장
#
#             if cost < distance[i[0]]: # 만약
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
#
#
# dijkstra(start)
#
# distance = [i for i in distance if i != INF]
# cnt = [i for i in graph[start]]
# print(len(cnt), max(distance))

# 미래도시
import heapq

n, m = map(int, input().split())
graph = [[] for i in range(m+1)]

for _ in range(m):  # 통로 정보 받기
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

x, k = map(int, input().split())

INF = 1e9 * n + 1
result = []


def dijkstra(start):
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

    distance = [i for i in distance if i != INF]
    result.append(max(distance))


dijkstra(k)
dijkstra(x)

print(sum(result))
