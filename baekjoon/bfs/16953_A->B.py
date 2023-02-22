import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())


def bfs(start):
    q = deque()
    q.append((start, 1))

    while q:
        c, d = q.popleft()
        if c > b:
            continue
        if c == b:
            print(d)
            break

        q.append((int(str(c) + "1"), d + 1))
        q.append((c * 2, d + 1))
    else:
        print(-1)


bfs(a)
