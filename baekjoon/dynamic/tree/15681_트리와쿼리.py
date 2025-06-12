import sys
sys.setrecursionlimit(10 ** 6)
n, r, q = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
d = [0 for _ in range(n + 1)]

def dfs(x):
    visited[x] = True
    d[x] = 1
    for i in graph[x]:
        if not visited[i]:
            dfs(i)
            d[x] += d[i]

dfs(r)
for _ in range(q):
    u = int(sys.stdin.readline())
    print(d[u])

