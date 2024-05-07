# 1388 바닥장식
# def tail(x, y) :
#     # - 인지 | 인지 판별
#     if li[x][y] == '-':
#         li[x][y] = 1
#
#         for _y in [1, -1]:
#             Y = y + _y
#             if (0 < Y < m) and li[x][Y] == '-':
#                 tail(x, Y)
#
#     if li[x][y] == '|':
#         li[x][y] = 1
#
#         for _x in [1, -1]:
#             X = x + _x
#             if (0 < X < n) and li[X][y] == '|':
#                 tail(X, y)
#
# n, m = map(int, input().split())
# li = []
# for i in range(n):
#     li.append(list(input()))
#
#
# result = 0
# for i in range(n):
#     for j in range(m):
#         if li[i][j] == '-' or li[i][j] == '|': #방문하지 않았을 경우만
#             result += 1
#
# print(result)

# 2210번 숫자판 점프
li = []
li2 = ['x']
for _ in range(5):
    li.append(list(input().split()))

def jump(x:int, y:int, cnt:int):
    if cnt == 5:
        return;
    if x <= -1 or x >= 5 or y <= -1 or y >= 5:
        return "X"

    jump(x - 1, y, cnt+1)  # 서
    jump(x, y - 1, cnt+1)  # 남
    jump(x + 1, y, cnt+1)  # 동
    jump(x, y + 1, cnt+1)  # 북




result = 0
for i in range(5):
    for j in range(5):
        cnt = 0
        string = ""
        jump(i, j, cnt)
        if string not in li2:
            result += 1
