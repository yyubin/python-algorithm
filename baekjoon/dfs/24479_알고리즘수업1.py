# 24479번 : 알고리즘 수업 - 깊이 우선 탐색1
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m, r = map(int, input().split())
visited = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()


cnt = 1


def dfs(graph, v, visited):
    global cnt
    visited[v] = cnt
    cnt += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


dfs(graph, r, visited)
print(*visited[1:], sep="\n")
