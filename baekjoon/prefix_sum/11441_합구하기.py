import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

for i in range(1, n):
    a[i] += a[i-1]

a.insert(0, 0)

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    print(a[y] - a[x-1])

