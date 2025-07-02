import sys
from collections import deque, defaultdict
n = int(sys.stdin.readline())
st = list(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+2)]
LOG = 21
parent = [[0] * LOG for _ in range(n+2)]
depth = [0] * (n+2)

dic = defaultdict(list)
pos_to_node = [0] * (2 * n+2)
stack = []
now = 1
for idx, ch in enumerate(st, 1):
    if ch == '0':
        node = now
        now += 1
        if stack:
            graph[stack[-1]].append(node)
        stack.append(node)
        dic[node].append(idx)
        pos_to_node[idx] = node
    else:
        node = stack.pop()
        dic[node].append(idx)
        pos_to_node[idx] = node

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

a_raw, b_raw = map(int, sys.stdin.readline().split())
a = pos_to_node[a_raw]
b = pos_to_node[b_raw]
p = lca(a, b)
i, j = dic[p]
print(min(i, j), max(i, j))


# a, b가 정점 번호라고 착각함
# 이진수 문자열의 인덱스(1-based)였음
#