import sys
from collections import deque, defaultdict
n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
LOG = 21
parent = [[0] * LOG for _ in range(n+1)]
depth = [0] * (n+1)
cost = defaultdict(int)
dist = [0] * (n+1)

for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    cost[(a, b)] = c
    cost[(b, a)] = c

def bfs(root):
    q = deque([root])
    depth[root] = 1
    while q:
        now = q.popleft()
        for next in graph[now]:
            if depth[next] == 0:
                depth[next] = depth[now] + 1
                parent[next][0] = now
                q.append(next)
                dist[next] += dist[now] + cost[(now, next)]

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

def get_kth(u, k):
    for i in range(LOG):
        if k & (1 << i):
            u = parent[u][i]
    return u


for _ in range(int(sys.stdin.readline())):
    li = list(map(int, sys.stdin.readline().split()))
    if li[0] == 1:
        l = lca(li[1], li[2])
        print(dist[li[1]] + dist[li[2]] - 2*dist[l])
    else:
        u, v, k = li[1], li[2], li[3]
        l = lca(u, v)
        dist_u = depth[u] - depth[l]
        if k <= dist_u + 1:
            print(get_kth(u, k-1))
        else:
            total = depth[u] + depth[v] - 2*depth[l] + 1
            kth = total - k
            print(get_kth(v, kth))

# get_kth는 k번 조상위로 넘어가고
# 크기 줄이기 위해서 u -> v가 k보다 크면 v -> total-k 만큼 가도록 수정

# k의 i번째 비트가 1이면
# u를 2^i 번째 조상으로 점프하는 것

# 쿼리 1 -> O(log N) lca + 수식
# 쿼리 2 -> O(log N) lca + 점프
# 전체 -> O(M log N)

# 아래처럼 찾으면 시간초과
# def get_path(u, v):
#     l = lca(u, v)
#
#     path_u, path_v = [], []
#     while u != l:
#         path_u.append(u)
#         u = parent[u][0]
#     while v != l:
#         path_v.append(v)
#         v = parent[v][0]
#
#     return path_u + [l] + path_v[::-1]