import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
start, end = 1e9, 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    start = min(start, c)
    end = max(end, c)

a, b = map(int, sys.stdin.readline().split())

def bfs(weight):
    global a, b
    q = deque()
    q.append(a)
    visited = [False] * (n+1)
    visited[a] = True

    while q:
        now = q.popleft()
        for i, w in graph[now]:
            if not visited[i] and w >= weight:
                visited[i] = True
                q.append(i)

    if visited[b]:
        return True
    else:
        return False

result = 0
while start <= end:
    mid = (start + end) // 2
    if bfs(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)

# 이분탐색 + bfs
# O(log w * (n + m))
# mst로도 가능
# 가장 무거운 간선 연결하면서 처음 a,b가 연결된 경우


# mst - 크루스칼
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    if x != y:
        parent[y] = x

edges = []

for _ in range(m):
    a, b, c = map(int,sys.stdin.readline().split())
    edges.append((c, a, b))

a, b = map(int, sys.stdin.readline().split())
edges.sort(reverse=True)
parent = [i for i in range(n+1)]

for w, a, b in edges:
    union(a, b)
    if find(a) == find(b):
        print(w)
        break

# 크루스칼 사용시
# 정렬 O(m log m)
# 크루스칼은 거의 O(1)
# 시간복잡도 O(m log m)

# 아니면 다익스트라로도 가능

# 크루스칼 사용시 간선을 내림차순 정렬
#
# 정렬된 간선:
# 4 --(6)-- 5
# 3 --(5)-- 4
# 1 --(4)-- 2
# 2 --(3)-- 3
# 1 --(2)-- 5

# 이렇게 있다고 가정했을때(a=1, b=5)
# 4, 5를 연결하고 a, b가 연결되어있는지 확인 -> 아직 안됨
# 3, 4 연결시 (3, 4, 5)연결
# 1, 2 연결시 (1, 2) , (3, 4, 5)
# 2, 3 연결시 (1, 2, 3, 4, 5) 연결 -> 여기에서 간선 중 최소 무게가 3이므로 3

# 가장 무거운 간들부터 연결하면서 a-b가 처음 연결되는 순간 그 시점의 간선이 최소값