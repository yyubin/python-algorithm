import sys
from itertools import combinations
from collections import defaultdict

n, s = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

result = 0
check = defaultdict(int)

def sub_sum(arr:list, check:defaultdict):
    for count in range(1, len(arr)+1):
        for comb in combinations(arr, count):
            c_sum = sum(comb)
            check[c_sum] += 1

sub_sum1 = defaultdict(int)
sub_sum2 = defaultdict(int)

sub_sum(li[n//2:], sub_sum1)
sub_sum(li[:n//2], sub_sum2)

result += sub_sum1[s] + sub_sum2[s]

for s1 in sub_sum1:
    if s-s1 in sub_sum2:
        result += sub_sum1[s1] * sub_sum2[s-s1]

print(result)

# def subsequences_sum(left, right, pos):
#     global result, check
#     result += li[left:right].count(s)
#     sums = []
#     for i in range(left, right):
#         length = len(sums)
#         for j in range(length):
#             sums.append(sums[j] + li[i])
#         sums.append(li[i])
#
#     for v in sums:
#         if pos == 0:
#             check[v] += 1
#         if pos == 1:
#             result += check[s - v]
#
#
# subsequences_sum(0, n // 2, 0)
# subsequences_sum(n // 2, n, 1)
# print(result)

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
