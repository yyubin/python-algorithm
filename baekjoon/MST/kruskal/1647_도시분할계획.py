import sys

n, m = map(int, sys.stdin.readline().split())

p = [i for i in range(n+1)]


def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]


def union(u, v):
    u = find(u)
    v = find(v)
    if u < v:
        p[v] = u
    else:
        p[v] = u


graph = []

for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))
    graph.append((b, a, c))

graph.sort(key=lambda x: x[2])


edges = 0
cost = 0
selected = []

for u, v, wt in graph:
    if find(u) != find(v):
        union(u, v)
        cost += wt
        edges += 1
        selected.append(wt)

cost -= selected.pop() #도시분할하기 때문에 마지막 간선제거
print(cost)
