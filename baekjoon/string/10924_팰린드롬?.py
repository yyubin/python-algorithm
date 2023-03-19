import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1
    if i < n-1 and li[i] == li[i+1]:
        dp[i][i+1] = 1

for i in range(1, n):
    for j in range(1, i+1):
        if li[i] == li[i-j] and dp[i-j+1][i-1] == 1:
            dp[i-j][i] = 1
# # 구간에 3 이상이라면 구간의 끝점값과 시작접값이 같고 나머지 구간이 팰린드롬이어야함

for _ in range(int(sys.stdin.readline())):
    s, e = map(int, sys.stdin.readline().split())
    print(dp[s-1][e-1])


# 인덱스 에러 고쳤지만 시간 초과 ㅎㅎ^^
# def palindrome(s, e):
#     if s == e:
#         return 1
#     if s+1 == e:
#         if li[s-1] == li[e-1]:
#             return 1
#         else:
#             return 0
#     if li[s - 1] != li[e - 1]:
#         return 0
#     return palindrome(s + 1, e - 1)

    # print(palindrome(s, e))

# 왜 인덱스에러인지 모르겠음..
# def palindrome(s, e):
#     if s == e:
#         return 1
#     if s+1 == e:
#         if li[s-1] == li[e-1]:
#             return 1
#         else:
#             return 0
#     if li[s - 1] != li[e - 1]:
#         return 0
#     return palindrome(s + 1, e - 1)

# 시간초과
#
#     tmp = li[s-1:e]
#     if tmp == tmp[::-1]:
#         print(1)
#     else:
#         print(0)
#
# # dp문제였음..
