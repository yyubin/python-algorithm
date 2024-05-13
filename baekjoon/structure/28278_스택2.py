import sys

stack = []
for _ in range(int(sys.stdin.readline())):
    li = list(map(int, sys.stdin.readline().split()))

    if li[0] == 1:
        stack.append(li[1])
    if li[0] == 2:
        print(stack.pop() if len(stack) != 0 else -1)
    if li[0] == 3:
        print(len(stack))
    if li[0] == 4:
        print(1 if len(stack) == 0 else 0)
    if li[0] == 5:
        print(stack[-1] if len(stack) != 0 else -1)

