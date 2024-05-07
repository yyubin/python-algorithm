# 9655번 : 돌게임
# num = int(input())
# cnt = 0
#
# while num > 0:
#     if (num - 3) <= 1:
#         cnt += 1
#         num -= 1
#     else:
#         cnt += 1
#         num -= 3
#
# print('SK' if cnt%2 == 0 else 'CY')
#
#
# N = int(input())
# print("CY" if N%2 else "SK")
#

# 9461번 : 파도반 수열

# cnt = int(input())
# num = []
#
# for k in range(cnt):
#     num.append(int(input()))
#
# for i in range(cnt):
#
#     d = [0] * (num[i]+1)
#     d[0] = 1
#     d[1] = 1
#     d[2] = 1
#
#     for j in range(3, num[i]):
#         d[j] = d[j-2] + d[j-3]
#
#     print(d[num[i] - 1])


d = [0] * 101
d[0] = 1
d[1] = 1
d[2] = 1

for j in range(3, 101):
    d[j] = d[j - 2] + d[j - 3]

num = int(input())

for i in range(num):
    p = int(input())
    print(d[p-1])

