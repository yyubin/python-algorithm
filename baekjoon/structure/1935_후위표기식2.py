import sys
n = int(sys.stdin.readline())
string = list(sys.stdin.readline().rstrip())

li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))

dic = {}
idx = 0
stack = []

for i in string:
    if i == '*':
        first = stack.pop()
        second = stack.pop()
        stack.append(second * first)
    elif i == '+':
        first = stack.pop()
        second = stack.pop()
        stack.append(second + first)
    elif i == '/':
        first = stack.pop()
        second = stack.pop()
        stack.append(second / first)
    elif i == '-':
        first = stack.pop()
        second = stack.pop()
        stack.append(second - first)
    else:
        if i not in dic:
            dic[i] = li[idx]
            idx += 1
        stack.append(dic[i])

print("{:.2f}".format(stack[0]))
