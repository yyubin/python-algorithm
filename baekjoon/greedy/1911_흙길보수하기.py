import sys
n, l = map(int, sys.stdin.readline().split())
puddles = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    puddles.append((a, b))
puddles.sort()

cnt = 0
now = 0

for s, e in puddles:
    if now >= e:
        continue

    if now < s:
        now = s

    while now < e:
        cnt += 1
        now += l

print(cnt)


# 웅덩이 크기가 10000이 아니었음
# import sys
# n, l = map(int, sys.stdin.readline().split())
# hole = [0] * 10001
#
# for _ in range(n):
#     a, b = map(int, sys.stdin.readline().split())
#
#     for i in range(a, b):
#         hole[i] = 'M'
#
# cnt = 1
# while True:
#     if 'M' not in hole:
#         break
#
#     now = hole.index('M')
#
#     for i in range(l):
#         if now+i < 10001:
#             hole[now+i] = cnt
#
#     cnt += 1
#
# print(cnt-1)
#
