import sys
for _ in range(int(sys.stdin.readline())):
    n, e = map(int, sys.stdin.readline().split())
    li = list(map(int, sys.stdin.readline().split()))

    gain = sum(li) * 2
    dp = [int(1e9)] * (gain+1)
    dp[0] = 0

    if gain < e:
        print("FULL")
        continue

    for i in li:
        max_ = i*2
        min_ = i

        for j in range(gain, max_-1, -1):
            dp[j] = min(dp[j], dp[j-max_] + min_)

    print(min([dp[i] for i in range(e, gain+1)]))
