import sys
input = sys.stdin.readline
from collections import deque, defaultdict

n = int(input())
graph = [[] for _ in range(n+1)]
LOG = 21
parent = [[0] * LOG for _ in range(n+1)]
depth = [0] * (n+1)
dist = [0] * (n+1)
cost = defaultdict(int)

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    cost[(a, b)] = c
    cost[(b, a)] = c

def bfs(root):
    q = deque([root])
    depth[root] = 1
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if depth[nxt] == 0:
                depth[nxt] = depth[cur] + 1
                parent[nxt][0] = cur
                q.append(nxt)
                dist[nxt] += dist[cur] + cost[(cur, nxt)]

bfs(1)

for j in range(1, LOG):
    for i in range(1, n+1):
        parent[i][j] = parent[parent[i][j-1]][j-1]

def lca(u, v):
    if depth[u] < depth[v]:
        u, v = v, u

    for i in reversed(range(LOG)):
        if depth[u] - (1 << i) >= depth[v]:
            u = parent[u][i]

    if u == v:
        return u

    for i in reversed(range(LOG)):
        if parent[u][i] != parent[v][i]:
            u = parent[u][i]
            v = parent[v][i]

    return parent[u][0]

q = int(input())
for _ in range(q):
    u, v = map(int, input().split())
    l = lca(u, v)
    print(dist[u] + dist[v] - 2*(dist[l]))
