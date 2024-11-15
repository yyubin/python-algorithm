import sys
for _ in range(int(sys.stdin.readline())):
    st = sys.stdin.readline().rstrip()
    left = []
    right = []
    for i in st:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)
    print(''.join(left+right[::-1]))

## 상태가 2개인 스택문제인 경우, 상태 두개를 스택 2개로 표현해서 푸는게 유리함

# 시간초과
# import sys
# for _ in range(int(sys.stdin.readline())):
#     st = list(sys.stdin.readline().rstrip())
#     idx = 0
#     result = [0] * len(st)
#     for i in st:
#         if i == '<':
#             idx -= 1
#             if idx < 0:
#                 idx = 0
#         elif i == '>':
#             idx += 1
#             if idx > len(st):
#                 idx = len(st)
#         elif i == '-':
#             idx -= 1
#             result[idx] = 0
#         else:
#             result.insert(idx, i)
#             idx += 1
#
#     for r in result:
#         if r != 0:
#             print(r, end="")
#
#
#
#
