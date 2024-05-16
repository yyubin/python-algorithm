import sys
d, k = map(int, sys.stdin.readline().split())
dp = [0 for _ in range(d+1)]
dp[0] = 0
dp[1] = 1
dp[2] = 1

while True:
    for i in range(3, d+1):
        dp[i] = dp[i-1] + dp[i-2]

    if dp[d] == k:
        print(dp[1])
        print(dp[2])
        break
    elif dp[-1] < k:
        dp[2] += 1
    else:
        dp[1] += 1
        dp[2] = dp[1]


# dp[d] = dp[d-1] + dp[d-2]
# dp[6] = 41
# dp[6] = dp[5] + dp[4]
# dp[6] = dp[4] + dp[3] + dp[4]
# dp[6] = dp[3] + dp[2] + dp[2] + dp[1] + dp[3] + dp[2]
# dp[6] = dp[2] + dp[1] + dp[2] + dp[2] + dp[1] + dp[2] + dp[1] + dp[2]
# dp[6] = 5 * dp[2] + 3 * dp[1]

# dp[7] = 218
# dp[7] = dp[6] + dp[5]
# dp[7] = 5 * dp[2] + 3 * dp[1] + dp[5]
# dp[7] = 5 * dp[2] + 3 * dp[1] + dp[4] + dp[3]
# dp[7] = 5 * dp[2] + 3 * dp[1] + dp[3] + dp[2] + dp[2] + dp[1]
# dp[7] = 5 * dp[2] + 3 * dp[1] + dp[2] + dp[1] + dp[2] + dp[2] + dp[1]
# dp[7] = 8 * dp[2] + 5 * dp[1]

# dp[1] = dp[1]
# dp[2] = dp[2]
# dp[3] = dp[1] + dp[2]
# dp[4] = dp[1] + 2*dp[2]
# dp[5] = 2*dp[1] + 3*dp[2]
# dp[6] = 3*dp[1] + 5*dp[2]
# dp[7] = 5*dp[1] + 8*dp[2]
# dp[8] = 8*dp[1] + 13*dp[2]
# dp[9] = 13*dp[1] + 21*dp[2]

