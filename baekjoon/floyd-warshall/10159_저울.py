import sys
INF = int(1e9)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = -1

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1
            if graph[i][k] == -1 and graph[k][j] == -1:
                graph[i][j] = -1

for i in range(1, n+1):
    print(graph[i].count(INF) - 1)

# 플로이드-워셜 응용..? 문제인듯 기본적으로 O(n^3)
# 비교관계를 표현해야 하므로 i > j 일때 graph[i][j] 를 1로두고 graph[j][i] = -1로 표현
# 최소 거리를 구하는게 아니고 graph[i][k] 가 1이고 graph[k][j]가 1이라는 것은 i < k < j 이므로 graph[i][j] 도 1로 표현
# graph[i][k] 가  -1이고 graph[k][j]가 -1이이면 i > k > j 이므로 graph[i][j] 는 -1

# 일단 모든 요소끼리의 대소관계를 구하기를 원했고, 그래프를 써야겠다는 생각은 났음 -> 플로이드-워셜
# 걍 하나의 관계 전체 관계에서의 최단거리나 찝어서 a,b의 대소관계 그런걸 원하면 다익스트라 써야 햇을 듯
# 응용할 때 대소관계를 알아야 하므로 간선방향을 명확히 해줘야함
# 근데 플로이드워셜 템플릿이 기억이 안나서 찾아봄