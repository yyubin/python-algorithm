import sys
from collections import deque
tc = int(sys.stdin.readline())

for _ in range(tc):
    n, k = map(int, sys.stdin.readline().rstrip().split())
    time = [0] + list(map(int, sys.stdin.readline().rstrip().split()))

    graph = [[] for _ in range(n+1)]
    degree = [0 for _ in range(n+1)]
    dp = [0 for _ in range(n+1)]
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append(b)
        degree[b] += 1

    w = int(sys.stdin.readline())

    q = deque()
    for i in range(1, n+1):
        if degree[i] == 0:
            q.append(i)
            dp[i] = time[i]

    while q:
        x = q.popleft()
        for i in graph[x]:
            degree[i] -= 1
            dp[i] = max(dp[x] + time[i], dp[i])
            if degree[i] == 0:
                q.append(i)

    print(dp[w])

#위상정렬
#https://freedeveloper.tistory.com/390




