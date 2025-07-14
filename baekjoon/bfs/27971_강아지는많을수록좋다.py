import sys
from collections import deque
n, m, a, b = map(int, sys.stdin.readline().split())
area = []
visited = [False] * (n+1)
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    area.append((i, j))


def bfs():
    q = deque()
    q.append((a, 1))
    q.append((b, 1))
    visited[a] = True
    visited[b] = True

    while q:
        now, cnt = q.popleft()
        if now == n:
            return cnt
        for i, j in area:
            if i <= now <= j:
                break
        else:
            if now + a <= n and not visited[now+a]:
                q.append((now+a, cnt+1))
                visited[now+a] = True
            if now + b <= n and not visited[now+b]:
                q.append((now+b, cnt+1))
                visited[now+b] = True

    return -1

print(bfs())