import sys
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]

dp[0][0] = graph[0][0]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        if i == 0:
            dp[i][j] = dp[i][j-1] + graph[i][j]
            continue
        if j == 0:
            dp[i][j] = dp[i-1][j] + graph[i][j]
            continue
        dp[i][j] = max(dp[i][j-1] + graph[i][j], dp[i-1][j] + graph[i][j], dp[i-1][j-1] + graph[i][j])

print(dp[n-1][m-1])

# 시간복잡도 O(N*M)