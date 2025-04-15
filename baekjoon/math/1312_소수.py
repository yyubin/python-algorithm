import sys
a, b, n = map(int, sys.stdin.readline().split())
dap = 0
for _ in range(n):
    a = (a%b) * 10
    dap = a//b
print(dap)
