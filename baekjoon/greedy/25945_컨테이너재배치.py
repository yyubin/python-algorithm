import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

s = sum(li)
avg = s // n

under = 0
over = 0

for i in li:
    if i < avg:
        under += avg - i
    elif i > avg + 1:
        over += i - (avg + 1)

print(max(over, under))

# import sys
# n = int(sys.stdin.readline())
# li = list(map(int, sys.stdin.readline().split()))
#
# start = 0
# end = 1e9
# result = 1e9
#
# def cal1(li, mid):
#     tmp_over, tmp_under = 0, 0
#     for i in li:
#         if mid - 1 == i or mid == i:
#             continue
#         if i > mid:
#             tmp_over += i - mid
#         elif i < mid:
#             tmp_under += mid - i - 1
#
#     return max(tmp_over, tmp_under)
#
# def cal2(li, mid):
#     tmp_over, tmp_under = 0, 0
#     for i in li:
#         if mid == i or mid + 1 == i:
#             continue
#         if i > mid:
#             tmp_over += i - mid - 1
#         elif i < mid:
#             tmp_under += mid - i
#
#     return max(tmp_over, tmp_under)
#
# while start <= end:
#     mid = (start + end) // 2
#     over = 0
#     minus = 0
#
#     for i in li:
#         minus += (mid - i) if mid > i else 0
#         over += (i - mid) if i > mid else 0
#
#     if 0 < over - minus < n:
#         result = min(result, min(cal1(li, mid), cal2(li, mid)))
#         end = mid - 1
#         continue
#
#     if 0 < minus - over < n:
#         result = min(result, min(cal1(li, mid), cal2(li, mid)))
#         start = mid + 1
#         continue
#
#     if minus < over:
#         start = mid + 1
#         continue
#
#     if over < minus:
#         end = mid - 1
#         continue
#
#
# print(int(result))



# 이분 탐색으로 풀 필요가 없음
# 걍 무조건 평균 근사치로 나오기 때문에.. 샤갈;;
# 답은 떨어지는데 시간초과
