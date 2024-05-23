import sys
n = int(sys.stdin.readline())
d = [0] * (n+1)

if n >= 2:
    d[2] = 1
if n >= 5:
    d[5] = 1

for i in range(2, n+1):
    if d[i-2] > 0:
        d[i] = d[i-2] + 1

for i in range(5, n+1):
    if d[i-5] > 0:
        d[i] = min(d[i], d[i-5] + 1)

print(d[n] if d[n] >= 1 else -1)

