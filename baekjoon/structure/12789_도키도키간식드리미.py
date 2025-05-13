import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
stack = []
idx = 1
for i in li:
    while stack and stack[-1] == idx:
        stack.pop()
        idx += 1

    if i != idx:
        stack.append(i)
    else:
        idx += 1

while stack and stack[-1] == idx:
    stack.pop()
    idx += 1

print("Nice" if not stack else "Sad")
