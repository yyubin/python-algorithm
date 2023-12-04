import sys
n = int(sys.stdin.readline())

d = [0] * (n+1)
d[0] = 1

if n >= 2:
    d[2] = 3

for i in range(4, n+1, 2):
    d[i] = d[i-2] * d[2]
    for j in range(0, i-2, 2):
        d[i] += d[j] * 2

print(d[n])
