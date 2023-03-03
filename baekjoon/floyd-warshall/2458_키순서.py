import sys
n, m = map(int, sys.stdin.readline().split())
graph = [([0] * (n)) for _ in range(n)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

result = 0
for i in range(n):
    ck = 0
    for j in range(n):
        ck += graph[i][j] + graph[j][i]
    if ck == (n-1):
        result += 1

print(result)