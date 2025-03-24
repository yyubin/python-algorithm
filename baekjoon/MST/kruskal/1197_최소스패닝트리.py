import sys
sys.setrecursionlimit(10**6)
v, e = map(int, sys.stdin.readline().split())
graph = []
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph.append((a, b, c))
graph.sort(key=lambda x: x[2])
parent = [i for i in range(v+1)]
def union(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def same_parent(a, b):
    return get_parent(a) == get_parent(b)


res = 0
for a, b, dist in graph:
    if not same_parent(a, b):
        union(a, b)
        res += dist

print(res)

# 최소 신장 트리(= 최소 스패닝 트리)
# 간선과 정점이 있으면 그래프
# 그래프에서 사이클이 발생하지 않고 모든 정점이 이어진 트리면 스패닝 트리
# 그중에서 가장 작은 가중치를 갖는게 최소 스패닝 트리

# dist가 작은 순으로 정렬
# 만약 부모가 다르다면 -> 사이클이 존재하지 않는다면
# 간선 적용하고 dist 추가 

# 간선 정렬 O(e log e)
# 유니온 파인드, 경로 압축 포함 O(E å(V)) mst를 만들면서 find, union을 e번 수행
# 경로 압축 사용하면 O(å(V))는 거의 상수이므로 O(log V)로 근사 가능
# O(e log e) + O(e å(v)) ≈ O(E log V)
# 왜냐면 O(e log e)에서 e <= v^2 이므로
# O(log e) = O(log v^2) = O(2 log v) = O(log v)
# 고로 O(e log v)
