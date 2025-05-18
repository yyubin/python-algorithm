# 이분탐색 모듈
import sys
import bisect
input = sys.stdin.readline

n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
b = [int(input()) for _ in range(m)]

a.sort()

for value in b:
    idx = bisect.bisect_left(a, value)
    if idx < n and a[idx] == value:
        print(idx)
    else:
        print(-1)

# 이분탐색
import sys
n, m = map(int, sys.stdin.readline().split())
a, b = [], []
for _ in range(n):
    a.append(int(sys.stdin.readline()))
for _ in range(m):
    b.append(int(sys.stdin.readline()))
a.sort()

def find_idx(x):
    left, right = 0, n-1
    res = -1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            res = mid
            right = mid - 1
        elif a[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return res

for i in b:
    print(find_idx(i))

# 시간초과
# 이분탐색 문제였음 ㅡㅜㅜ
# import sys
# n, m = map(int, sys.stdin.readline().split())
# a, b = [], []
# for _ in range(n):
#     a.append(int(sys.stdin.readline()))
# for _ in range(m):
#     b.append(int(sys.stdin.readline()))
# a.sort()
#
# for i in range(m):
#     if b[i] in a:
#         print(a.index(b[i]))
#     else:
#         print(-1)
#
