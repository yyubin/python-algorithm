import sys
n = int(sys.stdin.readline())
schedules = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
calendar = [0] * 366

for start, end in schedules:
    for day in range(start, end + 1):
        calendar[day] += 1

res = 0
width = 0
height = 0

for day in range(1, 366):
    if calendar[day]:
        width += 1
        height = max(height, calendar[day])
    elif width > 0:
        res += width * height
        width = 0
        height = 0

if width > 0:
    res += width * height

print(res)


# ws더러워서 다시 만듦
# 반례도 있음

# import sys
# from collections import defaultdict
# n = int(sys.stdin.readline())
# li = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
# li.sort()
#
# dic = defaultdict(int)
# calendar = [0] * 366
# tmp = {}
# dist = {}
# for i, j in li:
#     if not dic[i]:
#         dic[i] = i
#         tmp[i] = 0
#         dist[i] = 0
#     for k in range(i, j+1):
#         calendar[k] += 1
#         dic[k] = dic[i]
#
# for k, v in dic.items():
#     if v in tmp:
#         tmp[v] = max(tmp[v], calendar[k])
#     if v in dist:
#         dist[v] = k
#
# res = 0
# for k, v in dist.items():
#     res += ((v+1)-k) * tmp[k]
# print(res)
