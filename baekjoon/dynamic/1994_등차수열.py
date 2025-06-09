import sys
n = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(n)]
li.sort()
dp = [{} for _ in range(n)]
res = 1
for i in range(n):
    for j in range(i):
        d = li[i] - li[j]
        dp[i][d] = dp[j].get(d, 1) + 1
        res = max(dp[i][d], res)
print(res)



# 그리고 res = 1로 해야함 적어도 자기 자신 하나는 수열 가능


# li 최댓값이 10억이라 무조건 터짐
# dp = [[0 for _ in range(max(li)+1)] for _ in range(d)]
#
# for i in range(d):
#     dp[i][li[0]] = 1
#
# res = 0
# for i in range(d):
#     for j in range(1, n):
#         if li[j] - i >= 0:
#             dp[i][li[j]] = dp[i][li[j] - i] + 1
#         else:
#             dp[i][li[j] - i] = 1
#
#         res = max(res, dp[i][li[j]])
#
# print(res)


