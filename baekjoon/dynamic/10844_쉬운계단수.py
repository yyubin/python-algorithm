import sys
n = int(sys.stdin.readline())
d = [[0] * 10 for _ in range(n)]

for i in range(1, 10):
    d[0][i] = 1

for i in range(1, n):
    d[i][0] = d[i-1][1]
    d[i][9] = d[i-1][8]
    for j in range(1, 9):
        d[i][j] = d[i-1][j-1] + d[i-1][j+1]

print(sum(d[n-1]) % 1000000000)
