import sys
n, m = map(int, sys.stdin.readline().split())
graph = []
first = ()
for _ in range(m+1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph.append((a, b, c))

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x1, y1 = find(x), find(y)
    if x1 > y1:
        parent[y1] = x1
    else:
        parent[x1] = y1

def kruskal(priority):
    edges = sorted(graph, key=lambda x: x[2], reverse=priority)
    tmp = 0
    cnt = 0
    for a, b, c in edges:
        if find(a) != find(b):
            union(a, b)
            if c == 0:
                tmp += 1
            cnt += 1
            if cnt == n:
                break
    return tmp

parent = list(range(n + 1))
worst = kruskal(False)

parent = list(range(n + 1))
best = kruskal(True)

print(worst**2 - best**2)


# 오르막길이 1인줄 알고 세번 제출함tq
#

