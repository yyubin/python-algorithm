import sys

n, m = map(int, sys.stdin.readline().split())
parents = list(range(n))

def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if find(a) == find(b):
        print(i+1)
        exit(0)
    union(a, b)
else:
    print(0)

