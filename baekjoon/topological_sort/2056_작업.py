import sys
from collections import deque
n = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
degree = [0 for _ in range(n + 1)]
times = [0 for _ in range(n + 1)]
dp = [0] * (n+1)

for i in range(n):
    li = list(map(int, sys.stdin.readline().strip().split()))
    times[i+1] = li.pop(0)
    li.pop(0)
    for j in li:
        graph[j].append(i+1)
        degree[i+1] += 1

q = deque()
for i in range(1, n+1):
    if degree[i] == 0:
        q.append(i)
        dp[i] = times[i]

while q:
    now = q.popleft()
    for i in graph[now]:
        degree[i] -= 1
        dp[i] = max(dp[i], dp[now] + times[i])
        if degree[i] == 0:
            q.append(i)

print(max(dp))

#모든 선행 작업이 끝난 후 시작해야 하므로 가장 오래 걸리는 경로를 따라가야 함