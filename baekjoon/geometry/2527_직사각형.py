import sys


def branch(li):
    x1, y1, x2, y2 = map(int, li[:4])
    p1, q1, p2, q2 = map(int, li[4:])

    if x2 < p1 or p2 < x1 or q1 > y2 or y1 > q2:
        return 'd'

    if (x2 == p1 and y2 == q1) or (x2 == p1 and y1 == q2) or (x1 == p2 and y1 == q2) or (x1 == p2 and y2 == q1):
        return 'c'

    if p1 == x2 or x1 == p2 or y1 == q2 or y2 == q1:
        return 'b'

    return 'a'


for _ in range(4):
    li = list(map(int, sys.stdin.readline().split()))
    print(branch(li))


# 그냥 쌩구현인데
# 이런게제일귀찮다..................

# 조건 검사시 꼭짓점 검사부터하고
# 선분검사해야 함

# import sys
# for _ in range(4):
#     li = list(map(int, sys.stdin.readline().split()))
#     a, b = li[:4], li[4:]
#     flag = False
#
#     if a[1] > b[0] or a[3] > b[2]:
#         print('a')
#         flag = True
#     if flag:
#         continue
#
#     for i in range(2):
#         for j in range(2):
#             if (a[i], a[i+2]) == (b[j], b[j+2]):
#                 print('c')
#                 flag = True
#                 break
#     if flag:
#         continue
#
#     for i in a:
#         if i in b:
#             print('b')
#             flag = True
#             break
#     if flag:
#         continue
#
#     print('d')
#
