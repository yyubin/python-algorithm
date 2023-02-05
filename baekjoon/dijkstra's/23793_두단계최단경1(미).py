import heapq

n, m = map(int, input().split())
INF = int(1e9)

graph = [[] for i in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

x, y, z = map(int, input().split())


def dijkstra(start, end, active_y):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    if active_y:
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

    else:

        while q:
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue

            for i in graph[now]:
                cost = dist + i[1]
                if i[0] == y:
                    continue
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

        return distance[end]


pathz = []
pathz.append(dijkstra(x, y, True) + dijkstra(y, z, True))
pathz.append(dijkstra(x, z, False))

for i in pathz:
    if i == INF:
        print(-1, end=" ")
    else:
        print(i, end=" ")



## 뭐가다른거지..???????
import sys
import heapq

INF = sys.maxsize
n, m = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    nodes[a].append([b, c])
x, y, z = map(int, sys.stdin.readline().rstrip().split())

def Dijkstra(start, y_active= True):
    distances = [INF for _ in range(n+1)]
    distances[start] = 0
    pq = []
    heapq.heappush(pq, [0, start])

    if y_active:
        while pq:
            cur_cost, cur_node = heapq.heappop(pq)
            if distances[cur_node] < cur_cost: continue

            for next_node, next_cost in nodes[cur_node]:
                if distances[next_node] > cur_cost + next_cost:
                    distances[next_node] = cur_cost + next_cost
                    heapq.heappush(pq, [cur_cost + next_cost, next_node])
    else:
        while pq:
            cur_cost, cur_node = heapq.heappop(pq)
            if distances[cur_node] < cur_cost: continue

            for next_node, next_cost in nodes[cur_node]:
                if next_node == y: continue
                if distances[next_node] > cur_cost + next_cost:
                    distances[next_node] = cur_cost + next_cost
                    heapq.heappush(pq, [cur_cost + next_cost, next_node])
    return distances

distances_1 = Dijkstra(start=x, y_active=True)
distances_2 = Dijkstra(start=y, y_active=True)
distances_3 = Dijkstra(start=x, y_active=False)

answer1 = distances_1[y] + distances_2[z]
answer2 = distances_3[z]

if answer1 >= INF: print(-1, end= ' ')
else: print(answer1, end=' ')

if answer2 == INF: print(-1)
else: print(answer2)