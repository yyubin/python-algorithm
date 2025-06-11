import sys
sys.setrecursionlimit(10 ** 6)
n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

res = 0

def dfs(x, parent):
    global res
    max1, max2 = 0, 0
    for nxt, cost in graph[x]:
        if nxt == parent:
            continue
        d = dfs(nxt, x) + cost
        if d > max1:
            max1, max2 = d, max1
        elif d > max2:
            max2 = d

    res = max(res, max1 + max2)
    return max1

dfs(1, -1)
print(res)
