import sys
now = 0
while True:
    now += 1
    string = sys.stdin.readline().rstrip()
    if '-' in string:
        break
    res = 0
    stack = []
    for i in string:
        if i == '{':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                res += 1
                stack.append(i)

    res += len(stack) // 2
    print(f'{now}. {res}')