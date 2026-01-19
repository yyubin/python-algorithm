import sys
a, b = [], []

for _ in range(10):
    t = int(sys.stdin.readline())
    a.append(t)

for _ in range(10):
    t = int(sys.stdin.readline())
    b.append(t)

a.sort(reverse=True)
b.sort(reverse=True)

ar = sum(a[0:3])
br = sum(b[0:3])

print(f'{ar} {br}')