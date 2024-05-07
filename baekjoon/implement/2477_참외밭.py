import sys
from collections import deque
k = int(sys.stdin.readline())
li = []

for _ in range(6):
    a, b = map(int, sys.stdin.readline().split())
    li.append((a, b))

max_row = (0, 0)
max_col = (0, 0)

for dist, val in li:
    if (dist == 1 or dist == 2) and max_row[1] < val:
        max_row = (dist, val)
    if (dist == 3 or dist == 4) and max_col[1] < val:
        max_col = (dist, val)

q = deque(li)
row_idx = li.index(max_row)
col_idx = li.index(max_col)
rotate_ = min(row_idx, col_idx)
q.remove(max_row)
q.remove(max_col)
q.rotate(-rotate_)
print(((max_row[1]*max_col[1])-(q[1][1]*q[2][1]))*k)





# 동 서 남 북
# 1 2 3 4
