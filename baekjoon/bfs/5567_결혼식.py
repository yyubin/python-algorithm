import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = []
for i in graph[1]:
    if i not in cnt:
        cnt.append(i)
    for j in graph[i]:
        if j not in cnt and j != 1:
            cnt.append(j)

print(len(cnt))

# bfs 문제이지만 그냥 간단하게 풀어봄



