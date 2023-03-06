import sys
n = int(sys.stdin.readline())
graph = [[sys.maxsize] * (n+1) for _ in range(n+1)]

while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1:
        break
    graph[a][b] = 1
    graph[b][a] = 1
    # a에서 b까지의 거리 1
    # b에서 a까지의 거리 1

for i in range(1, n+1):
    graph[i][i] = 0
    # 자기 자신으로 가는 것은 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == 1 or graph[i][j] == 0:
                continue
            elif graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

res = []
for i in range(1, n+1):
    res.append(max(graph[i][1:]))
    # 각 레코드별로 최솟값

_min = min(res) # 전체 최솟값
print(_min, res.count(_min)) # 최솟값 가진 후보 수

for i, v in enumerate(res):
    if v == _min:
        print(i+1, end=' ') # 최솟값 가진 후보 번호 출력

