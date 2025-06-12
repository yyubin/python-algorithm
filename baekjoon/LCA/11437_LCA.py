import sys
sys.setrecursionlimit(10**4)
n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

LOG = 21
parent = [[0] * LOG for _ in range(n+1)]
depth = [0] * (n+1)

def dfs(x, par):
    depth[x] = depth[par] + 1
    parent[x][0] = par
    for i in graph[x]:
        if i != par:
            dfs(i, x)

dfs(1, 0)

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
            v = parent[v][i]
            u = parent[u][i]

    return parent[u][0]

output = []
for _ in range(int(sys.stdin.readline())):
    u, v = map(int, sys.stdin.readline().split())
    output.append(str(lca(u, v)))

sys.stdout.write('\n'.join(output))

# parent[i][j] i의 2^j번째 조상
# parent[i][j] = parent[parent[i][j-1]][j-1] j번째 조상 = (j-1번째 조상의 j-1번째 조상)
# 2의 제곱 단위 점프를 만들어 log 시간에 올라가기 위함