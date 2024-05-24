import sys

ans = 0
for _ in range(int(sys.stdin.readline())):
    string = sys.stdin.readline().rstrip()

    stack = []
    for i in string:
        if not stack:
            stack.append(i)
            continue

        if stack[-1] == i:
            stack.pop()

        else:
            stack.append(i)

    if not stack:
        ans += 1

print(ans)
