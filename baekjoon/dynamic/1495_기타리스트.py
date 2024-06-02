import sys
n, s, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

d = [[0] * (m+1) for _ in range(n+1)]
d[0][s] = 1

for i in range(1, n+1):
    for j in range(m+1):
        if d[i-1][j] > 0:
            if 0 <= j+li[i-1] <= m:
                d[i][j+li[i-1]] = 1

            if 0 <= j-li[i-1] <= m:
                d[i][j-li[i-1]] = 1

res = -1
for i in range(m+1):
    if d[n][i] == 1:
        res = i

print(res)

