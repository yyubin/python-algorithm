import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
li = {}

for _ in range(n+m):
    a, b = map(int, sys.stdin.readline().split())
    li[a] = b

def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = [False] * 101
    visited[start] = True

    while q:
        now, cnt = q.popleft()
        if now == 100:
            return cnt
        for i in range(1, 7):
            if 0 <= now + i < 101 and not visited[now+i]:
                visited[now+i] = True
                if now+i in li:
                    q.append((li[now+i], cnt+1))
                else:
                    q.append((now+i, cnt+1))

print(bfs(1))
