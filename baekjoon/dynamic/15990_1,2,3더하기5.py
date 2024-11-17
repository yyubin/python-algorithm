import sys
d = [[0] * 4 for _ in range(100001)]
d[1][1] = 1
d[2][2] = 1
d[3][3] = 1
d[3][1] = 1
d[3][2] = 1
for i in range(4, 100001):
    d[i][1] = (d[i - 1][2] + d[i - 1][3]) % 1000000009
    d[i][2] = (d[i - 2][1] + d[i - 2][3]) % 1000000009
    d[i][3] = (d[i - 3][1] + d[i - 3][2]) % 1000000009
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    print(sum(d[n])%1000000009)

