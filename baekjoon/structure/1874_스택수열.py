import sys
n = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(n)]

stack = []
current = 1
result = []

for num in li:
    while current <= num:
        stack.append(current)
        result.append("+")
        current += 1

    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        sys.exit()

print(*result, sep="\n")


# import sys
# n = int(sys.stdin.readline())
# li = [int(sys.stdin.readline()) for _ in range(n)]
#
# idx = li.index(n)
# for i in range(idx+1, n):
#     if li[i-1] < li[i]:
#         print("NO")
#         sys.exit()
#
# visited = [i+1 for i in range(n)]
# stack = []
#
# for i in li:
#     if len(stack) == 0:
#         stack.append(visited.pop(0))
#         print("+")
#
#     if stack[-1] < i:
#         while stack[-1] != i:
#             stack.append(visited.pop(0))
#             print("+")
#         print("-")
#         stack.pop()
#     elif stack[-1] == i:
#         print("-")
#         stack.pop()
#     else:
#         while stack[-1] != i:
#             stack.pop()
#             print("-")
#         print("-")
#         stack.pop()
#
#
