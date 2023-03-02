import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

stack = []
result = [-1 for _ in range(n)]

for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        result[stack.pop()] = a[i]
    stack.append(i)

print(*result)

# 시간 초과
# result = []
# for i in range(n):
#     for j in range(i+1, n):
#         if a[i] < a[j]:
#             result.append(a[j])
#             break
#     else:
#         result.append(-1)
#
# print(*result)