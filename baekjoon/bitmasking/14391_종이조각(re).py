import sys
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
res = 0

for bit in range(1 << (n*m)):
    total = 0
    for i in range(n):
        row = 0
        for j in range(m):
            idx = i * m + j
            if bit & (1 << idx) != 0:
                row = row * 10 + graph[i][j]
            else:
                total += row
                row = 0
        total += row

    for j in range(m):
        col = 0
        for i in range(n):
            idx = i * m + j
            if bit & (1 << idx) == 0:
                col = col * 10 + graph[i][j]
            else:
                total += col
                col = 0
        total += col
    res = max(total, res)
print(res)
