import sys
n, k = map(int, sys.stdin.readline().split())
coins = []

for _ in range(n):
    coins.append(int(sys.stdin.readline()))

dp = [0 for _ in range(k+1)]
dp[0] = 1

for i in coins:
    for j in range(i, k+1):
        if j-1 >= 0:
            dp[j] += dp[j-i]

print(dp[k])