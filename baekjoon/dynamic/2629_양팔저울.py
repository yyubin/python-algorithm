import sys
num_weights = int(sys.stdin.readline())
weights = list(map(int, sys.stdin.readline().split()))
num_marbles = int(sys.stdin.readline())
marbles = list(map(int, sys.stdin.readline().split()))
dp = [[0]*(30*500+1) for _ in range(num_weights+1)]

result = set()

def get_result(weights, n, now, left, right):
    new = abs(left-right)

    if new not in result:
        result.add(new)

    if now == n:
        return 0

    if dp[now][new] == 0:
        get_result(weights, n, now+1, left+weights[now], right)
        get_result(weights, n, now+1, left, right+weights[now])
        get_result(weights, n, now+1, left, right)
        dp[now][new] = 1

get_result(weights, num_weights, 0, 0, 0)
ans = []

for marble in marbles:
    if marble in result:
        ans.append('Y')
    else:
        ans.append('N')

print(*ans)