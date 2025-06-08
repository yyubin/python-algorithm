import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = []

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph.append((a, b, c))
graph.sort(key= lambda x: x[2])

parent = [i for i in range(n+1)]
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