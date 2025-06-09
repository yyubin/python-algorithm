import sys
n, m = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
roads = set()

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'Y':
            roads.add((min(i, j), max(i, j)))

if len(roads) < m:
    print(-1)
    sys.exit()

roads = sorted(roads)
parent = [i for i in range(n)]

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    x = find(a)
    y = find(b)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

res = [0] * n
mst_edges = set()
cnt = 0
for i, j in roads:
    if find(i) != find(j):
        union(i, j)
        res[i] += 1
        res[j] += 1
        cnt += 1
        mst_edges.add((i, j))

if cnt != n-1:
    print(-1)
    sys.exit()

add = 0
for i, j in roads:
    if add >= m - (n-1):
        break
    if (i, j) not in mst_edges:
        res[i] += 1
        res[j] += 1
        add += 1

print(*res)

# 간선 m개를 무조건 구성해줘야 하니까
# mst 만들고 순회 안한 곳들 추가로 더해줘야함(총 m개만큼만)