import sys
d, m = map(int, sys.stdin.readline().split())

if d % 2 == 1:
    print(0)
    exit()

n = d//2
dp = [[0] * (n+2) for _ in range(d+1)]

dp[1][1] = 1

for i in range(2, d+1):
    for j in range(n+1):
        if i < d and j == 0:
            continue
        if j > 0:
            dp[i][j] += dp[i-1][j-1]
        if j < n:
            dp[i][j] += dp[i-1][j+1]
        dp[i][j] %= m
print(dp[d][0])


# 정확히 d칸을 이동해서 다시 고도 0으로 돌아오는 경로의 수 (음수 고도 X)
# 중간에 고도 0이 되지 않는 카탈란 경로