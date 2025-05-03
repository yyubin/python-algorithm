import sys
n = int(sys.stdin.readline())
graph = [[] for _ in range(n)]

for i in range(n):
    tmp = list(sys.stdin.readline())
    for j in range(n):
        if tmp[j] == 'N':
            graph[i].append(0)
        else:
            graph[i].append(1)

res = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if i == j:
            continue
        if graph[i][j] == 1:
            cnt += 1
        else:
            for k in range(n):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    cnt += 1
                    break
    res = max(res, cnt)
print(res)