import sys
from itertools import combinations
n, s = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))


# 시간초과
# cnt = 0
#
# for i in range(1, n+1):
#     comb = combinations(li, i)
#
#     for x in comb:
#         if sum(x) == s:
#             cnt += 1
#
# print(cnt)

# 틀렸움
# left = 0
# right = n
# result = 0
#
# while left < right:
#     tmp = li[left:right]
#     if sum(tmp) > s:
#         right -= 1
#     elif sum(tmp) < s:
#         left += 1
#     else:
#         result += 1
#         right -= 1
#         left += 1
#
# print(result)

