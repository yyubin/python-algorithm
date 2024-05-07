# DFS 전 재귀개념이 모자란듯하여 추가 문제 풀이

# 24460 : 특별상이라도 받고 싶어

# n = int(input())
# li = []
# li2 = []
# for _ in range(n):
#     li.append(list(map(int, input().split())))
#
# def re(n:int):
#     if n == 2:
#         li2.sort()
#         return li2[1]
#     else:
#         n //= 2
#

# 10872:팩토리얼
num = int(input())


def re(n):

    if n == 0 or n == 1:
        return 1

    return n * re(n - 1)


print(re(num))
