# 11725번 : 트리의 부모 찾기
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
visited = [False] * (n+1)
parent = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            parent[i] = v
            dfs(graph, i, visited)

dfs(graph, 1, visited)
print(*parent[2:], sep="\n")