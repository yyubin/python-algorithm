import sys
n = int(sys.stdin.readline())
li = [tuple(map(int, input().split())) for _ in range(n)]

def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

total = 0
for i in range(1, n):
    total += dist(li[i-1], li[i])

min_total = float('inf')
for i in range(1, n-1):
    skip = dist(li[i-1], li[i]) + dist(li[i], li[i+1])
    direct = dist(li[i-1], li[i+1])
    new_total = total - skip + direct
    min_total = min(min_total, new_total)

print(min_total)

# res = 0
# sum_ = 0
# last_x, last_y = 0, 0
# idx = 0
# li = []
# for i in range(n):
#     x, y = map(int, sys.stdin.readline().split())
#     li.append((x, y))
#     if 0 < i < n-1:
#         now_x = abs(x - last_x)
#         now_y = abs(y - last_y)
#         dist = now_x + now_y
#         if res < dist:
#             res = dist
#             idx = i
#         last_x, last_y = x, y
#
# last_x, last_y = li[0][0], li[0][1]
# for i in range(n):
#     x, y = li[i][0], li[i][1]
#     if i != idx:
#         now_x = abs(x - last_x)
#         now_y = abs(y - last_y)
#         dist = now_x + now_y
#         sum_ += dist
#         last_x, last_y = x, y
# print(sum_)

# 그리디 아님
# 완탐