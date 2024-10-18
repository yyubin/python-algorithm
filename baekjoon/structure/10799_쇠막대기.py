import sys
stick = sys.stdin.readline().rstrip()
stack = []
cnt = 0

for i in range(len(stick)):
    if stick[i] == '(':
        stack.append('(')
    else:
        if stick[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1

print(cnt)
