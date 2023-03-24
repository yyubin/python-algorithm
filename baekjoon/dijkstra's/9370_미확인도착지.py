import sys
from heapq import heappop, heappush
tc = int(sys.stdin.readline())

def dijkstra(start):
    heap = []

    distance = [sys.maxsize for _ in range(n+1)]
    heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        dist, now = heappop(heap)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(heap, (cost, i[0]))

    return distance

for _ in range(tc):
    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    destination = []
    for _ in range(t):
        destination.append(int(sys.stdin.readline()))

    s_ = dijkstra(s)
    g_ = dijkstra(g)
    h_ = dijkstra(h)

    result = []
    for i in destination:
        if s_[g] + g_[h] + h_[i] == s_[i] or s_[h] + h_[g] + g_[i] == s_[i]:
            result.append(i)
    result.sort()
    print(*result)

# g와 h를 무조건 지나야함
# 출발 -> g -> h -> 도착
# 출발 -> h -> g -> 도착
# 최단 거리 구해주고 그 최단거리 중 하나가 출발 -> 도착 최단거리와 같으면 저장