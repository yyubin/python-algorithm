import sys
n, m = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
row = [0]
col = [0]
for i in range(k):
    a, b = map(int, sys.stdin.readline().split())
    if a == 0:
        row.append(b)
    else:
        col.append(b)
row.sort()
col.sort()
row.append(m)
col.append(n)

row_ = 0
for i in range(1, len(row)):
    row_ = max(row_, row[i] - row[i-1])
col_ = 0
for i in range(1, len(col)):
    col_ = max(col_, col[i] - col[i-1])
print(row_*col_)

