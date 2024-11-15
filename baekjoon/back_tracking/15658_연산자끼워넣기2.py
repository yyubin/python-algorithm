import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
oper = list(map(int, sys.stdin.readline().split()))
max_, min_ = -sys.maxsize, sys.maxsize

def bt(i, ans, add, sub, mul, div):
    global max_, min_
    if i >= n:
        max_ = max(max_, ans)
        min_ = min(min_, ans)
        return
    if add > 0:
        bt(i+1, ans+li[i], add-1, sub, mul, div)
    if sub > 0:
        bt(i+1, ans-li[i], add, sub-1, mul, div)
    if mul > 0:
        bt(i+1, ans*li[i], add, sub, mul-1, div)
    if div > 0:
        bt(i+1, ans//li[i] if ans > 0 else -((-ans)//li[i]), add, sub, mul, div-1)


bt(1, li[0], oper[0], oper[1], oper[2], oper[3])
print(max_)
print(min_)

# 시간초과 그리고 string 말고 index로 비교하는게 나을듯
# import sys
# from itertools import permutations
# n = int(sys.stdin.readline())
# li = list(map(int, sys.stdin.readline().split()))
# oper = list(map(int, sys.stdin.readline().split()))
# opers = []
# tmp = ['+', '-', '*', '/']
#
# for i, v in enumerate(oper):
#     for j in range(v):
#         opers.append(tmp[i])
#
# max_, min_ = 0, sys.maxsize
# for i in permutations(opers, n-1):
#     tmp_res = li[0]
#     for j in range(len(i)):
#         if i[j] == '+':
#             tmp_res += li[j+1]
#         if i[j] == '-':
#             tmp_res -= li[j+1]
#         if i[j] == '*':
#             tmp_res *= li[j+1]
#         if i[j] == '/':
#             tmp_res //= li[j+1]
#
#     min_ = min(tmp_res, min_)
#     max_ = max(tmp_res, max_)
#
# print(max_)
# print(min_)




