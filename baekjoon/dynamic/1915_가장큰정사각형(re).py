import sys
n, m = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

d = [[0] * m for i in range(n)]
ans = 0

for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            d[i][j] = graph[i][j]
        elif graph[i][j] == 0:
            d[i][j] = 0
        else:
            d[i][j] = min(d[i-1][j-1], d[i-1][j], d[i][j-1]) + 1

        ans = max(d[i][j], ans)

print(ans * ans)

