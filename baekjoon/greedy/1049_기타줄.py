import sys
n, m = map(int, sys.stdin.readline().split())
six = []
one = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    six.append(a)
    one.append(b)

min_six = min(six)

ans = 0

while n > 0:
    if n >= 6:
        ans += min(6*min(one), min_six)
        n -= 6
    else:
        tmp = min(n*min(one), min_six)
        ans += tmp
        n = 0

print(ans)

