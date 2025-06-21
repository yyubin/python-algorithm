import sys
def solve(a, b, n, m):
    p = [-1] * (m+2)
    s = [n] * (m+2)

    ai = 0
    for bi in range(1, m + 1):  # b[0] ~ b[m-1] → p[1] ~ p[m]
        while ai < n and a[ai] < b[bi - 1]:
            ai += 1
        if ai == n:
            break
        p[bi] = ai
        ai += 1

    ai = n - 1
    for bi in range(m, 0, -1):  # b[m-1] ~ b[0] → s[m] ~ s[1]
        while ai >= 0 and a[ai] < b[bi - 1]:
            ai -= 1
        if ai < 0:
            break
        s[bi] = ai
        ai -= 1

    res = sys.maxsize
    for i in range(1, m + 1):
        if p[i - 1] < s[i + 1]:
            res = min(res, b[i - 1])

    if p[m] != -1:
        return 0
    elif res == sys.maxsize:
        return -1
    else:
        return res


for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    print(solve(a, b, n, m))


# 이분탐색 안됨
# import sys
# def solve_bs(a, b, n, m):
#     def check(k):
#         i = j = 0
#         used = False
#         while i < n and j < m:
#             if a[i] >= b[j]:
#                 i += 1
#                 j += 1
#             elif not used and k >= b[j]:
#                 used = True
#                 j += 1
#             else:
#                 i += 1
#         if j < m and not used and k >= b[j]:
#             j += 1
#         print(k, j, used)
#         return j == m
#
#     if check(0):
#         return 0
#
#     left = 1
#     right = max(b) + 1
#     answer = -1
#
#     while left <= right:
#         mid = (left + right) // 2
#         print("mid", mid)
#         if check(mid):
#             answer = mid
#             right = mid - 1
#         else:
#             left = mid + 1
#
#     return answer


# def chk_possible(a, b, l):
#     if not b:
#         return l
#     idx = 0
#     for i in a:
#         if idx < len(b) and b[idx] <= i:
#             idx += 1
#             l -= 1
#             if idx == len(b):
#                 break
#     return l
#
# def chk_first(a, b, l):
#     if not b:
#         return l
#     idx = 0
#     for i in a:
#         if idx < len(b) and b[idx] <= i:
#             idx += 1
#             l -= 1
#             if idx == len(b):
#                 break
#         else:
#             return idx
#     return idx
#
# def bs():
#     left = 0
#     right = max(b) + 1
#     res = 0
#
#     while left <= right:
#         mid = (left + right) // 2
#         ok = False
#
#
#         if ok:
#             res = mid
#             right = mid - 1
#         else:
#             left = mid + 1
#     return res
#
# for _ in range(int(sys.stdin.readline())):
#     n, m = map(int, sys.stdin.readline().split())
#     a = list(map(int, sys.stdin.readline().split()))
#     b = list(map(int, sys.stdin.readline().split()))
#     chk = chk_possible(a, b, m)
#     if chk <= 0:
#         print(0)
#     else:
#         tmp = b.copy()
#         tmp.remove(max(b))
#         chk = chk_possible(a, tmp, m-1)
#         if chk <= 0:
#             print(bs())
#         else:
#             print(-1)
#
#
#
