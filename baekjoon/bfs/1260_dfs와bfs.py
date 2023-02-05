from collections import deque
import sys

input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

start1, start2 = v, v

for _ in range(m):
    c, d = map(int, input().split())
    graph[c].append(d)
    graph[d].append(c)

for i in range(len(graph)):
    graph[i].sort()


cnt = 1
cnt1 = 1

def dfs(graph, v, visited):
    global cnt
    visited[v] = cnt
    cnt += 1
    print(v, end=" ")
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)


def bfs(graph, v, visited):
    queue = deque([v])
    global cnt1
    visited[v] = cnt1
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                cnt1 += 1
                visited[i] = cnt1

visited = [0] * (n + 1)
dfs(graph, start1, visited)

print()

visited = [0] * (n + 1)
bfs(graph, start2, visited)


