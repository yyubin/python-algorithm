import sys
n, m = map(int, sys.stdin.readline().split())
graph = []
origin = 0
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    origin += c
    graph.append((a, b, c))

if n-1 > m:
    print(-1)
    sys.exit()

parent = [i for i in range(n+1)]
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b

graph.sort(key=lambda x: x[2])
cnt = 0
tmp = 0
for a, b, c in graph:
    if find(a) != find(b):
        union(a, b)
        tmp += c
        cnt += 1
        if cnt == n-1:
            break

for i in range(2, n+1):
    if find(i) != find(1):
        print(-1)
        sys.exit()

print(origin-tmp)
