import sys
n, m = map(int, sys.stdin.readline().split())
graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = -1
    graph[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == 0:
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                elif graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1


k = int(sys.stdin.readline())
for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    print(graph[a][b])