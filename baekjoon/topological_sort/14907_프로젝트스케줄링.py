import sys
from collections import deque
graph = {}
degree = {}
times = {}

while True:
    try:
        li = list(map(str, sys.stdin.readline().rstrip().split()))
        if li[0] not in graph:
            graph[li[0]] = []
        degree[li[0]] = 0
        if len(li) > 2:
            for i in li[2]:
                if i not in graph:
                    graph[i] = [li[0]]
                else:
                    graph[i].append(li[0])
                degree[li[0]] += 1
        times[li[0]] = int(li[1])
    except:
        break

for node in degree:
    if node not in graph:
        graph[node] = []

d = {}
q = deque()

for k, v in degree.items():
    d[k] = 0
    if v == 0:
        q.append(k)
        d[k] = times[k]

while q:
    now = q.popleft()
    for i in graph[now]:
        degree[i] -= 1
        d[i] = max(d[i], d[now] + times[i])
        if degree[i] == 0:
            q.append(i)

print(max(d.values()))
