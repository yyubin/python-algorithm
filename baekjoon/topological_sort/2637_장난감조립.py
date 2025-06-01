import sys
from collections import deque
n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
degree = [0 for _ in range(n+1)]
dp = [0 for _ in range(n+1)]
dp[n] = 1
chk = [False] * (n+1)
for _ in range(int(sys.stdin.readline())):
    x, y, k = map(int, sys.stdin.readline().split())
    graph[x].append((y, k))
    degree[y] += 1
    chk[x] = True

q = deque()
for i in range(1, n+1):
    if degree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    for nxt, nxt_dist in graph[now]:
        degree[nxt] -= 1
        dp[nxt] += nxt_dist * dp[now]
        if degree[nxt] == 0:
            q.append(nxt)

for i in range(1, n+1):
    if not chk[i]:
        print(i, dp[i])
