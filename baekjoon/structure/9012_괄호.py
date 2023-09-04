import sys
t = int(sys.stdin.readline())

for _ in range(t):
    li = list(sys.stdin.readline().rstrip())
    stack = []

    for i, v in enumerate(li):
        if i == 0 and v == ')':
            stack.append(1)
            break
        if v == '(':
            stack.append(v)
        else:
            if len(stack) == 0:
                stack.append(1)
                break
            else:
                stack.pop()

    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
