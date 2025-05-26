import sys
n = int(sys.stdin.readline())
orchard = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
d = [[0 for _ in range(n)] for _ in range(n)]
res = float('-inf') ## 음수로 초기화
for i in range(n):
    for j in range(n):
        res = max(orchard[i][j], res)
        if i == j == 0:
            d[i][j] = orchard[i][j]
        elif i == 0:
            d[i][j] = orchard[i][j] + d[i][j-1]
        elif j == 0:
            d[i][j] = orchard[i][j] + d[i-1][j]
        else:
            d[i][j] = orchard[i][j] + d[i][j-1] + d[i-1][j] - d[i-1][j-1]

for window in range(1, n+1):
    for i in range(n-window+1):
        for j in range(n-window+1):
            x1, y1 = i, j
            x2, y2 = i+window-1, j+window-1
            total = d[x2][y2]

            if x1 > 0:
                total -= d[x1-1][y2]
            if y1 > 0:
                total -= d[x2][y1-1]
            if x1 > 0 and y1 > 0:
                total += d[x1-1][y1-1]

            res = max(res, total)
print(res)