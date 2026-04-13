import sys
r, c, q = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]

for i in range(r):
    for j in range(c):
        if i == 0 and j == 0:
            continue

        if i == 0:
            arr[i][j] += arr[i][j-1]
            continue
        if j == 0:
            arr[i][j] += arr[i-1][j]
            continue

        arr[i][j] += (arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1])

for _ in range(q):
    r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1

    res = arr[r2][c2]

    if c1 > 0:
        res -= arr[r2][c1-1]

    if r1 > 0:
        res -= arr[r1-1][c2]

    if r1 > 0 and c1 > 0:
        res += arr[r1-1][c1-1]

    print(res // ((r2-r1+1) * (c2-c1+1)))

