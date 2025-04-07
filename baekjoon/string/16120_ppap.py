import sys
s = sys.stdin.readline().rstrip()
stack = []

for c in s:
    stack.append(c)
    if len(stack) >= 4 and stack[-4:] == ['P', 'P', 'A', 'P']:
        for _ in range(4):
            stack.pop()
        stack.append('P')
if stack == ['P']:
    print('PPAP')
else:
    print('NP')