import sys
from collections import deque
n = int(sys.stdin.readline())
indegree = [0] * (n+1)
cost = [0] * (n+1)
graph = [[] for _ in range(n+1)]
d = [0] * (n+1)

for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    tmp.pop()
    cost[i+1] = tmp.pop(0)

    for j in tmp:
        graph[j].append(i+1)
        indegree[i+1] += 1
def topology_sort():
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            d[i] = cost[i]

    while q:
        now = q.popleft()

        for k in graph[now]:
            indegree[k] -= 1
            d[k] = max(d[k], d[now] + cost[k])
            if indegree[k] == 0:
                q.append(k)

    print(*d[1:], sep="\n")

topology_sort()

# 간선있어야함
# 사이클없어야함
# 간선방향(의존하는게 있는지)