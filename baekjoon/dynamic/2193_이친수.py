import sys
n = int(sys.stdin.readline())
d = [0] * (n+1)
d[1] = 1

for i in range(2, n+1):
    d[i] = d[i-2] + d[i-1]

print(d[n])
