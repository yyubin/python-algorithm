import sys
n = int(sys.stdin.readline())
d = []

for _ in range(n):
    d.append(list(map(int, sys.stdin.readline().split())))


for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            d[i][0] += d[i-1][0]
        elif j == i:
            d[i][j] += d[i-1][j-1]
        else:
            d[i][j] += max(d[i-1][j-1], d[i-1][j])

print(max(d[n-1]))

