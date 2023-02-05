# 개미전사
# n = int(input())
# li = list(map(int, input().split()))
#
# d = []
# idx = 0
#

# def dynamic(idx: int, num: int):  # 0, 3
#     if idx + 1 >= num or num >= n:  # 0 + 1 >= 3 false
#         return
#     d.append(li[idx] + li[num])  # li[0] + li[3] num은 -1한후 다시 호출
#     dynamic(idx, num - 1)
#
#
# for i in range(n):
#     dynamic(i, n-1)
#
# print(d)
# print(max(d))

# 1로 만들기

# div = [15, 10, 6, 5, 3, 2]
# li = [(num // div[i]) + (num % div[i]) for i in range(len(div))]
# pos = [i for i, x in enumerate(li) if x == min(li)]
# result = []
#
# num = num // div[2]
#
# print(li)
#
# print(pos)
# num = int(input())
# cnt = 0
# d = [5, 3, 2]
#
#
# def div(n: int):
#     global cnt
#     print(cnt, n)
#     if n == 1:
#         return
#
#     l1 = [num // d[i] for i in range(len(d))]
#     a = n // l1[l1.index(min(l1))]
#
#     if a <= 0:
#         cnt += 1
#         div(n - 1)
#     else:
#         cnt += 1
#         div(a)
#
#
# div(num)
#
# print(cnt+1)

# x = int(input())
#
# d = [0]*(x+1)
#
# for i in range(2, x+1):
#     d[i] = d[i-1] + 1
#     if i % 2 == 0:
#         d[i] = min(d[i], d[i // 2] + 1)
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i // 3] + 1)
#
#
# print(d[x])

# 효율적인 화폐 구성
# a, x = map(int, input().split())
# li = []
# for i in range(a):
#     li.append(int(input()))
#
# li.sort(reverse=True)
#
# d = [0]*(x+1)
# d[0] = 0
#
# for i in range(1, x+1):
#     for j in li:
#         print(i, j, i//j)
#         if i % j == 0 or i % j in li:
#             d[i] += i // j
#
# print(d)
# print(d[x])

# 금광 캐기

cnt = int(input())

while cnt > 0:

    n, m = map(int, input().split())  # 3, 4
    li = []

    li2 = list(map(int, input().split()))

    for i in range(len(li2) // m):
        li.append(li2[i * m:(i * m) + m])

    sum = 0
    print(li)

    for i in range(m):  # 4
        temp = []
        for j in range(n):  # 3
            temp.append(li[j][i])
        sum += max(temp)

    print(sum)
    cnt -= 1
