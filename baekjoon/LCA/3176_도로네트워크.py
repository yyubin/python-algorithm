import sys
from collections import defaultdict, deque
n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
cost = defaultdict(int)
for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    cost[(a, b)] = c
    cost[(b, a)] = c

LOG = 21
parent = [[0] * LOG for _ in range(n+1)]
parent_max = [[0] * LOG for _ in range(n+1)]
parent_min = [[sys.maxsize] * LOG for _ in range(n+1)]
depth = [0] * (n+1)

def bfs(root):
    q = deque([root])
    depth[root] = 1
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if depth[nxt] == 0:
                depth[nxt] = depth[now] + 1
                parent[nxt][0] = now
                parent_max[nxt][0] = cost[(nxt, now)]
                parent_min[nxt][0] = cost[(nxt, now)]
                q.append(nxt)

bfs(1)

for j in range(1, LOG):
    for i in range(1, n+1):
        parent[i][j] = parent[parent[i][j-1]][j-1]
        parent_max[i][j] = max(parent_max[i][j-1], parent_max[parent[i][j-1]][j-1])
        parent_min[i][j] = min(parent_min[i][j-1], parent_min[parent[i][j-1]][j-1])

def lca(u, v):
    max_, min_ = 0, sys.maxsize
    if depth[u] < depth[v]:
        u, v = v, u

    for i in reversed(range(LOG)):
        if depth[u] - (1 << i) >= depth[v]:
            tmp = parent[u][i]
            max_ = max(parent_max[u][i], max_)
            min_ = min(parent_min[u][i], min_)
            u = tmp
    if u == v:
        return (min_, max_)

    for i in reversed(range(LOG)):
        if parent[u][i] != parent[v][i]:
            max_ = max(max_, parent_max[u][i], parent_max[v][i])
            min_ = min(min_, parent_min[u][i], parent_min[v][i])
            u = parent[u][i]
            v = parent[v][i]

    res = (
        min(min_, parent_min[u][0], parent_min[v][0]),
        max(max_, parent_max[u][0], parent_max[v][0])
    )
    return res

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    print(*lca(a, b))


# 어려워
