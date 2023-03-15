import sys

n = int(sys.stdin.readline())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
li.sort(key=lambda x: x[0])
d = [1] * n

for i in range(n):
    for j in range(i):
        if li[i][1] > li[j][1]:
            d[i] = max(d[i], d[j] + 1)

print(n - max(d))

# n = int(sys.stdin.readline())
# li = []
# li2 = []
# d = [0 for _ in range(n)]
#
# for _ in range(n):
#     li.append(list(map(int, sys.stdin.readline().split())))
# li.sort(key=lambda x: x[0])
#
# for i in range(n):
#     li2.append(li[i][1])
#
# for i in range(n):
#     for j in range(n):
#         if li2[i] > li2[j] and d[i] < d[j]:
#             d[i] = d[j]
#     d[i] += 1
#
# print(n - max(d))
