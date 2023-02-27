import sys
v, e = map(int, sys.stdin.readline().split())
graph = []

p = [i for i in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))
    graph.append((b, a, c))

graph.sort(key=lambda x: x[2])
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


edges = 0
cost = 0
selected = []

for u, v, wt in graph:
    if find(u) != find(v):
        union(u, v)
        cost += wt
        edges += 1
        selected.append(wt)

print(cost)