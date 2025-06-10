import sys
n, m, k = map(int, sys.stdin.readline().split())
graph = []
plant = list(map(int, sys.stdin.readline().split()))

parent = [i for i in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph.append((a, b, c))


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    if x in plant:
        parent[y] = x
    elif y in plant:
        parent[x] = y
    else:
        if x > y:
            parent[y] = x
        else:
            parent[x] = y

graph.sort(key= lambda x: x[2])
res = 0
cnt = 0
for a, b, c in graph:
    a_p = find(a)
    b_p = find(b)
    if a_p != b_p:
        if a_p in plant and b_p in plant:
            continue
        else:
            union(a, b)
            res += c
            cnt += 1

            if cnt == n-k:
                break
print(res)

