import sys
from collections import deque

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

q = deque()
for i in range(n):
    q.append((i+1, li[i]))

ans = []
while q:
    x, y = q.popleft()
    ans.append(x)
    if y > 0:
        q.rotate(-(y-1))
    else:
        q.rotate(abs(y))

print(*ans)
