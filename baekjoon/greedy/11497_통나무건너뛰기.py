import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    li = list(map(int, sys.stdin.readline().split()))
    li.sort()

    left_stack = []
    right_stack = []

    for i in range(n):
        if i % 2 == 0:
            left_stack.append(li.pop())
        else:
            right_stack.append(li.pop())
    left_stack.sort()
    result = left_stack + right_stack

    res = 0
    for i in range(n - 1):
        res = max(abs(result[i] - result[i + 1]), res)

    print(res)

