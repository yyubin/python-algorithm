import sys
from collections import deque
n = int(sys.stdin.readline())
visited = set()

q = deque()
q.append((1, 0, 0))
visited.add((1, 0, 0))

while q:
    now, bff, cnt = q.popleft()
    if now == n:
        print(cnt)
        break

    if now != bff:
        t = (now, now, cnt+1)
        if t not in visited:
            q.append(t)

    if bff and 0 <= now + bff <= 2000:
        t = (now+bff, bff, cnt+1)
        if t not in visited:
            visited.add(t)
            q.append(t)

    if 0 <= now-1 and (now-1):
        t = (now-1, bff, cnt+1)
        if t not in visited:
            visited.add(t)
            q.append(t)

