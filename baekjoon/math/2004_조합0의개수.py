import math
import sys

n, m = map(int, sys.stdin.readline().split())

def cnt2(num):
    if num < 2:
        return 0

    cnt = 0
    while num >= 2:
        cnt += num//2
        num = num//2
    return cnt

def cnt5(num):
    if num < 5:
        return 0

    cnt = 0
    while num >= 5:
        cnt += num//5
        num = num//5
    return cnt

two = cnt2(n) - cnt2(n-m) - cnt2(m)
five = cnt5(n) - cnt5(n-m) - cnt5(m)
print(min(two, five))


# ans = list(str(math.factorial(n)//(math.factorial(m)*math.factorial(n-m))))
#
# cnt = 0
# for i in range(len(ans) - 1):
#     if ans[len(ans) - 1 - i] == '0':
#         cnt += 1
#     else:
#         print(cnt)
#         break

