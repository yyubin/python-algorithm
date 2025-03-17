import sys
INF = int(1e9)
n, m = map(int, sys.stdin.readline().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

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

cnt = 0
mid = (n+1) // 2

for i in range(1, n+1):
    heavy = sum(1 for j in range(1, n+1) if graph[i][j] == 1)
    light = sum(1 for j in range(1, n+1) if graph[i][j] == -1)

    if heavy >= mid or light >= mid:
        cnt += 1

print(cnt)

## 10159_저울과 유사한 문제
# 시간 복잡도 O(N^3)
# 중간 값이라는게 최상위 최하위가 아닌 모든 중간을 의미하는게 아니라 확실한 중간값이기 어려운
# 것만 찾으면 되는 문제 였음
