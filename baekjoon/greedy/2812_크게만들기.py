import sys
n, k = map(int, sys.stdin.readline().split())
nums = sys.stdin.readline().rstrip()
stack = []

for num in nums:
    while stack and stack[-1] < num and k > 0:
        stack.pop()
        k -= 1
    stack.append(num)

if k > 0:
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))

## https://jokerldg.github.io/algorithm/2021/05/25/make-big.html
