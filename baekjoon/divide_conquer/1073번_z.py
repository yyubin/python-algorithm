# import sys
#
# n, r, c = map(int, sys.stdin.readline().split())
# graph = [[[] for _ in range(2 ** n)] for _ in range(2 ** n)]
#
# print(graph)
#
#
# # x, y
# # x+1, y
# # x, y+1
# # x+1, y+1
#
#
# x = 0
# y = 0
#
# def re(x, y, v):
#     print(x, y, v)
#     graph[x][y] = v
#     v += 1
#     graph[x + 1][y] = v
#     v += 1
#     graph[x][y + 1] = v
#     v += 1
#     graph[x + 1][y + 1] = v
#     v += 1
#     return v


# (0, 0)
# (0, 2)
# (2, 0)
# (2, 2)
# value = 0
# print(2 ** n)
# for i in range(2 ** n):
#     value = re(x, y, value)
#
#     x += 2
#     y += (2 ** n) - 1
#
# print(graph)

import sys

n, r, c = map(int, sys.stdin.readline().split())
cnt = 0

while n != 0:
    n -= 1
    if r < 2**n and c < 2**n: # 1사분면
        cnt += (2**n) * (2**n) * 0

    elif r < 2**n <= c: # 2사분면
        cnt += (2**n) * (2**n) * 1
        c -= (2**n)

    elif r >= 2**n > c: # 3사분면
        cnt += (2**n) * (2**n) * 2
        r -= (2**n)

    else: # 4사분면
        cnt += (2**n) * (2**n) * 3
        c -= (2**n)
        r -= (2**n)

# n이 0이 될때까지 사분면을 확인해서 cnt에 계속 더해줌
print(cnt)
