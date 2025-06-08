import sys
n = int(sys.stdin.readline())
graph = []
for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    graph.append((i, a, b, c))

edges = []
for dim in range(1, 4):
    graph.sort(key= lambda x: x[dim])
    for i in range(n-1):
        a, b = graph[i][0], graph[i+1][0]
        cost = abs(graph[i][dim] - graph[i+1][dim])
        edges.append((cost, a, b))

edges.sort()

parent = [i for i in range(n)]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(u, v):
    u = find(u)
    v = find(v)
    if u < v:
        parent[v] = u
    else:
        parent[u] = v

res = 0
for cost, a, b in edges:
    if not find(a) == find(b):
        union(a, b)
        res += cost
print(res)

# 행성들을 각각 x, y, z 좌표 기준으로 정렬
# 인접한 두 행성 간의 간선만 추가 (|x1 - x2|, |y1 - y2|, |z1 - z2|)
# 이렇게 하면 N-1개씩 × 3축 = 총 3(N - 1)개의 간선만 고려

# 이미 x, y, z 축으로 정렬해다면, 가까운 것들끼리 인접해있으므로 인접한것들끼리만 비교해도 ㄱㅊ
# 좌표압축을 이 방법으로 하는 것이고 2중 for문으로 검사 불가 (최대 100,000개)
# 크루스칼 시간복잡도 : O(e log e)
# union-find가 거의 1