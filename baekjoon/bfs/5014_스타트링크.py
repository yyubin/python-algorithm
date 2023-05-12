import sys
from collections import deque
f, s, g, u, d = map(int, sys.stdin.readline().split())
visited = [-1] * (f+1)

q = deque()
q.append((s, 0))

while q:
    now, cnt = q.popleft()
    if now == g:
        print(cnt)
        sys.exit(0)
    for i in [u, -d]:
        next = now + i
        if 0 < next <= f and visited[next] == -1:
            q.append((next, cnt+1))
            visited[next] = 0

print("use the stairs")
