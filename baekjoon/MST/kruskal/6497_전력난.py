import sys

def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]


def union(u, v):
    u = find(u)
    v = find(v)
    if u > v:
        p[u] = v
    else:
        p[v] = u


while True:
    m, n = map(int, input().split())

    if m == 0 and n == 0:
        break
    graph = []
    p = [i for i in range(m + 1)]

    for _ in range(n):
        a, b, c = map(int, sys.stdin.readline().split())
        graph.append((a, b, c))

    graph.sort(key=lambda x: x[2])

    cost = 0

    for u, v, wt in graph:
        if find(u) != find(v):
            union(u, v)
        else:
            cost += wt

    print(cost)
