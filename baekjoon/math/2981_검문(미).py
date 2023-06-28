import sys
import math
n = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(n)]

r = [li[i] - li[i-1] for i in range(1, n-1)]
print(r)

gcds = []
for i in range(1, len(r)-1):
    gcds.append(math.gcd(r[i], r[i-1]))

print(gcds)






# def gcd(a, b):
#     while b > 0:
#         a, b = b, a%b
#     return a
#
#
# li.sort()
# x = li.pop()
# result = []
# while li:
#     x = gcd(x, li.pop())
#     if x != 1:
#         result.append(x)
#
# print(*result)