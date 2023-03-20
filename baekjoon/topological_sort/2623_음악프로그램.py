import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    tmp = list(map(int, sys.stdin.readline().split()))
    for i in range(1, tmp[0]):
        graph[tmp[i]].append(tmp[i+1])
        indegree[tmp[i+1]] += 1

def topologoy_sort():
    result = []
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    if len(result) != n:
        print(0)
    else:
        print(*result, sep="\n")

topologoy_sort()
