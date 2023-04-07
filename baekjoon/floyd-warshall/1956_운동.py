import sys
v, e = map(int, sys.stdin.readline().split())
graph = [[int(1e9)] * (v+1) for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

result = 1e9
for i in range(1, v+1):
    result = min(result, graph[i][i])

if result == 1e9:
    print(-1)
else:
    print(result)


# 크루스칼로는 풀 수 없음, 플로이드-워셜 문제
# graph.sort(key=lambda x: x[2])
# def find(u):
#     if u != p[u]:
#         p[u] = find(p[u])
#     return p[u]
#
#
# def union(u, v):
#     u = find(u)
#     v = find(v)
#     if u < v:
#         p[v] = u
#     else:
#         p[v] = u
#
#
# edges = 0
# cost = 0
# selected = []
#
# for u, v, wt in graph:
#     if find(u) != find(v):
#         union(u, v)
#         cost += wt
#         edges += 1
#         selected.append(wt)
#
# print(edges)
# print(selected)
# print(cost)
