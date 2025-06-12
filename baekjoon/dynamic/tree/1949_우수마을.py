import sys
sys.setrecursionlimit(10 ** 6)
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

d = [[0, 0] for _ in range(n+1)]
visited = [False] * (n+1)

def dfs(x):
    visited[x] = True
    d[x][1] = li[x-1]

    for i in graph[x]:
        if not visited[i]:
            dfs(i)
            d[x][0] += max(d[i][1], d[i][0])
            d[x][1] += d[i][0]

dfs(1)
print(max(d[1][0], d[1][1]))