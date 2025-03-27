import sys
from collections import deque
n = int(sys.stdin.readline())
q = deque()
now = []
res = 0

for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    if tmp[0] == 1:
        if now:
            q.append(now)
        now = [tmp[1], tmp[2]]
    if now:
        now[1] -= 1
        if now[1] == 0:
            res += now[0]
            if q:
                now = q.pop()

print(res)