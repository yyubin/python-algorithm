import sys
from collections import deque
def bfs():
    q = deque()
    q.append((home_x, home_y))
    while q:
        x, y = q.popleft()
        if abs(x-festival_x) + abs(y-festival_y) <= 1000:
            print('happy')
            return
        for i in range(n):
            if not visited[i]:
                nx, ny = li[i]
                if abs(x-nx) + abs(y-ny) <= 1000:
                    visited[i] = 1
                    q.append((nx, ny))
    print('sad')
    return


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    home_x, home_y = map(int, sys.stdin.readline().split())
    li = []
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        li.append((x, y))

    festival_x, festival_y = map(int, sys.stdin.readline().split())
    visited = [0 for _ in range(n+1)]
    bfs()