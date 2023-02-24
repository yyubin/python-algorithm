import sys
n, m = map(int, sys.stdin.readline().split())
graph = [[sys.maxsize for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = [0] * (n+1)
for i in range(1, n+1):
    for j in range(1, n+1):
        if i != j:
            result[i] += graph[i][j]

print(result.index(min(result[1:])))



## 플로이드-워셜
# https://chanhuiseok.github.io/posts/algo-50/