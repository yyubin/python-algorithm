import sys
n, start, end, m = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((a, b, c))
benefit = list(map(int, sys.stdin.readline().split()))

def bf(start):
    infinite_nodes = set()
    distance[start] = benefit[start]
    for i in range(n):
        for j in range(m):
            cur, next, cost = edges[j]
            if distance[cur] == -sys.maxsize:
                continue

            new_value = distance[cur] - cost + benefit[next]

            if distance[next] < new_value:
                distance[next] = new_value
                if i == n - 1:
                    infinite_nodes.add(next)
    return infinite_nodes

distance = [-sys.maxsize] * n
cycle = bf(start)

def can_reach_end(from_nodes):
    visited = [False] * n
    q = list(from_nodes)
    while q:
        now = q.pop()
        visited[now] = True
        for a, b, c in edges:
            if a == now and not visited[b]:
                q.append(b)
    return visited[end]

if can_reach_end(cycle):
    print("Gee")
else:
    if distance[end] == -sys.maxsize:
        print("gg")
    else:
        print(distance[end])
