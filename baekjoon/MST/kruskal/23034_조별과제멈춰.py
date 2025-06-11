import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 6)
n, m = map(int, sys.stdin.readline().split())

graph = []

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph.append((a, b, c))

graph.sort(key=lambda x: x[2])

k = int(sys.stdin.readline())
leaders = [tuple(map(int, sys.stdin.readline().split())) for _ in range(k)]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root, y_root = find(x), find(y)
    if x_root < y_root:
        parent[y_root] = x_root
    else:
        parent[x_root] = y_root

mst_e = defaultdict(list)
cnt = 0
tmp = 0
parent = [i for i in range(n+1)]
for a, b, c in graph:
    a_ = find(a)
    b_ = find(b)
    if a_ != b_:
        union(a, b)
        mst_e[a].append((b, c))
        mst_e[b].append((a, c))
        cnt += 1
        tmp += c
        if cnt == n-1:
            break

def dfs(cur, target, visited, max_cost):
    if cur == target:
        return True, max_cost

    visited[cur] = True
    for nxt, cost in mst_e[cur]:
        if not visited[nxt]:
            found, result = dfs(nxt, target, visited, max(max_cost, cost))
            if found:
                return True, result
    return False, 0

for a, b in leaders:
    visited = [False] * (n+1)
    _, cost = dfs(a, b, visited, 0)
    print(tmp - cost)


# mst 생성해서 두 그룹으로 쪼갤때 가장 비싼 간선 제거
# dfs로 경로 탐색해야함
# 경로상 최고 cost 구하는거는 dfs가 bfs보다 나음

# LCA 쓰는게 낫다는데 아직 모름 pass..
