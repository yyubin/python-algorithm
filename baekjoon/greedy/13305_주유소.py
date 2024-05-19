import sys
n = int(sys.stdin.readline())
cost = list(map(int, sys.stdin.readline().split()))
station = list(map(int, sys.stdin.readline().split()))
station.pop()

dist = 0
gas = 0

for now in range(n-1):
    if gas < cost[now]:
        next_min = 1
        for i in range(now+1, len(cost)):
            if station[i] >= station[now]:
                next_min += 1
            else:
                break
        for i in range(now, now + next_min):
            dist += station[now] * cost[i]
            gas += cost[i]
    gas -= cost[now]

print(dist)


# 9
# 1 2 3 4 5 6 7 8
# 10 3 2 3 15 2 10 8 1

# 10
# 6
# 6 + 8 + 10 + 12 + 14 + 16

# 82