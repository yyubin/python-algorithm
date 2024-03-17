import sys
graph = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(4):
    ax, ay, bx, by = map(int, sys.stdin.readline().split())
    for i in range(ax, bx):
        for j in range(ay, by):
            graph[i][j] = 1

cnt = 0
for i in graph:
    cnt += sum(i)

print(cnt)
