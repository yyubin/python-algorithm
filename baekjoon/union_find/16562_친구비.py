import sys
sys.setrecursionlimit(10**6)
n, m, k = map(int, sys.stdin.readline().split())
cost = list(map(int, sys.stdin.readline().split()))
friends = [i for i in range(n+1)]
cost.insert(0, 0)

def find(a):
    if friends[a] != a:
        friends[a] = find(friends[a])
    return friends[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        if cost[a] <= cost[b]:
            friends[b] = a
        else:
            friends[a] = b


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    union(a, b)

result = 0
for i, v in enumerate(friends):
    if i == v:
        result += cost[i]


if result > k:
    print("Oh no")
else:
    print(result)
