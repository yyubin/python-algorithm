import sys
n, k = map(int, sys.stdin.readline().split())
coins = []

for _ in range(n):
    coins.append(int(sys.stdin.readline()))

dp = [sys.maxsize for _ in range(k+1)]
dp[0] = 0

for i in coins:
    # 1, 5, 12
    for j in range(i, k+1):
        dp[j] = min(dp[j], dp[j-i] + 1)

print(-1 if dp[k] == sys.maxsize else dp[k])
