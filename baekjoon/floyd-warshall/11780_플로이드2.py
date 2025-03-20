import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[int(1e9)] * (n+1) for _ in range(n+1)]
path = [[()]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = min(graph[a][b], c)
    path[a][b] = (a, b)

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                path[i][j] = path[i][k] + path[k][j][1:]

for i in range(1, n+1):
    for j in range(1, n+1):
        print(0 if graph[i][j] == int(1e9) else graph[i][j], end=" ")
    print()

for i in range(1, n+1):
    for j in range(1, n+1):
        print(len(path[i][j]), *path[i][j])

# 네 너무 어렵죠..?
# 플로이드 워셜 경로 저장문제
# 비용은 그냥 플로이드 워셜 사용하면 되고
# 모든 경로에 대한 다른 경로들의 경우를 구해야하니까 플로이드 써야함
# 경로는 최초에 path[a][b] = (a, b) 이렇게 초기화 해뒀다가
# k 거치는게 짧을 경우
# path[a][b] = path[a][k] + path[k][b][1:]
# 1부터인건 k가 겹치니까
#
# 시간복잡도
# O(N^3)

