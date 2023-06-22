import sys
from bisect import bisect_left
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().rstrip().split()))

LIS = [a[0]]

for i in a:
    if LIS[-1] < i:
        LIS.append(i)
    else:
        idx = bisect_left(LIS, i)
        LIS[idx] = i

print(len(LIS))

# DP로 푼 예시인데 시간초과 남 ㅎㅎ
# LIS 이분탐색은 nlogn이기 때문에 이분탐색으로 풀겠다
# import sys
# n = int(sys.stdin.readline())
# li = list(map(int, sys.stdin.readline().split()))
# d = [0] * (n+1)
#
# for i in range(n):
#     for j in range(n):
#         if li[i] > li[j] and d[i] < d[j]:
#             d[i] = d[j]
#     d[i] += 1
#
# print(max(d))


# greedy 인 줄 알았는데 dp로 풀어야 함 (LIS)
# abs가 적은쪽이 무조건 더 많은 플래그를 꼽을 수 있도록 보장해주지 못함
# import sys
# n = int(sys.stdin.readline())
# li = list(map(int, sys.stdin.readline().split()))
#
# result = []
# for i in range(n):
#     print(result)
#     if not result:
#         result.append((i+1, li[i]))
#         continue
#
#     flag = False
#     for j in result:
#         if li[i] <= j[1]:
#             flag = True
#             if abs((i+1) - li[i]) < abs(j[0] - j[1]):
#                 result.remove((j[0], j[1]))
#                 result.append((i+1, li[i]))
#
#     if not flag:
#         result.append((i+1, li[i]))
#
# print(result)
# print(len(result))
