import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
li = [0] + list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
d = [[0, li[i]]*2 for i in range(n+1)]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(now):
    visited[now] = True
    for v in graph[now]:
        if not visited[v]:
            dfs(v)
            d[now][1] += d[v][0]
            d[now][0] += max(d[v][0], d[v][1])

dfs(1)
print(max(d[1][1], d[1][0]))

