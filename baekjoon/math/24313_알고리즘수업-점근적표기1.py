import sys
f, g = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
n = int(sys.stdin.readline())

if (f*n + g) <= c*n and f <= c:
    print(1)
else:
    print(0)


# 음수 보장 안됨
# import sys
# f, g = map(int, sys.stdin.readline().split())
# c = int(sys.stdin.readline())
# n = int(sys.stdin.readline())
#
# def ck(f, g, c, n):
#     for i in range(n, 101):
#         if f*n+g >= c*n:
#             return 0
#     return 1
#
# print(ck(f, g, c, n))
