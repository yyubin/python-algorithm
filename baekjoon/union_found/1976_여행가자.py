import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
parents = list(range(n))
plan = list(map(int, sys.stdin.readline().split()))


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


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union(i, j)

ans = 'YES'
for i in range(1, m):
    if parents[plan[i] - 1] != parents[plan[0] - 1]:
        ans = 'NO'
        break

print(ans)

# 태그 열고 풀었움..!