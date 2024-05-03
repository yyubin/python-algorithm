import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
q = deque([i+1 for i in range(n)])
res = []

while q:
    q.rotate(-k)
    res.append(q.pop())

print('<', end='')
print(*res, sep=', ', end='')
print('>')



# 1 2 3 4 5 6 7
# 4 5 6 7 1 2
# 7 1 2 4 5
# 4 5 7 1
# 1 4 5
# 1 4 (1)
# 4   (4)
