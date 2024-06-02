import sys
n = int(sys.stdin.readline())

x, y = 0, 1
for _ in range(n):
    x, y = (x+y)%1000000007, x%1000000007

print(x)
