import sys
import heapq
n = int(sys.stdin.readline())
graph = []
visited = [[False] * n for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

def dijkstra():
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    heap = []
    heapq.heappush(heap, [0, 0, 0])
    visited[0][0] = True

    while heap:
        a, x, y = heapq.heappop(heap)
        if x == n-1 and y == n-1: #n-1, n-1까지 가는 최단경로
            print(a)
            return
        for i in range(4):
            ddx = dx[i] + x
            ddy = dy[i] + y
            if 0 <= ddx < n and 0 <= ddy < n and not visited[ddx][ddy]:
                visited[ddx][ddy] = True
                if graph[ddx][ddy] == 0: #검은방 방문시에는 a에 1추가
                    heapq.heappush(heap, [a+1, ddx, ddy])
                else:
                    heapq.heappush(heap, [a, ddx, ddy])

dijkstra()
