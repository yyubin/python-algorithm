import sys
n, m = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline()) for _ in range(n)]
future = [[-1] * m for _ in range(n)]

for i in range(n):
    cloud = 0
    for j in range(m):
        if graph[i][j] == 'c':
            cloud = 1
        elif cloud >= 1:
            cloud += 1
        if cloud >= 1:
            future[i][j] += cloud

for i in future:
    print(*i)
