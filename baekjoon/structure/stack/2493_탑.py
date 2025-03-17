import sys
n = int(sys.stdin.readline())
top = list(map(int, sys.stdin.readline().split()))
stack = []
res = [0] * n

for i in range(n):
    while stack and stack[-1][1] < top[i]:
        stack.pop()

    if stack:
        res[i] = stack[-1][0] + 1

    stack.append([i, top[i]])

print(*res)

## 출력 포맷 틀려서 제출만 4번함..
# 잘 확인하자..
# 스택 활용 O(N)


# O(N^2) 시간 초과
# import sys
# from collections import deque
# n = int(sys.stdin.readline())
# top = list(map(int, sys.stdin.readline().split()))
# left = []
# right = deque(top)
# res = []
# while right:
#     now = right.popleft()
#     for i, v in enumerate(left[::-1]):
#         if now <= v:
#             res.append(len(left) - i)
#             break
#     else:
#         res.append(0)
#     left.append(now)
# print(res)
#
#
#
