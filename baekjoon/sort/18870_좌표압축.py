import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

set_ = sorted(list(set(li)))
dic = {set_[i]: i for i in range(len(set_))}
for i in li:
    print(dic[i], end=" ")


## 시간초과
# import sys
# n = int(sys.stdin.readline())
# li = list(map(int, sys.stdin.readline().split()))
# result = []
#
# for i in range(n):
#     stack = []
#     for j in li:
#         if li[i] > j and j not in stack:
#             stack.append(j)
#     result.append(len(stack))
#
# print(*result)
