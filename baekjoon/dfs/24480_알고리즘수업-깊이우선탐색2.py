import sys
sys.setrecursionlimit(10**6)
n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 1

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort(reverse=True)

def dfs(x):
    global cnt
    visited[x] = cnt
    for i in graph[x]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

dfs(r)
print(*visited[1:], sep="\n")
