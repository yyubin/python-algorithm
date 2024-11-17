import sys
from collections import deque
n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dir_x = [1, 0]
dir_y = [0, 1]

q = deque()
visited[0][0] = True
val = graph[0][0]
q.append((0, 0, val))
while q:
    x, y, jump = q.popleft()
    for i in range(2):
        dx = x + dir_x[i] * jump
        dy = y + dir_y[i] * jump
        if 0 <= dx < n and 0 <= dy < n and not visited[dx][dy]:
            visited[dx][dy] = True
            if dx == n-1 and dy == n-1:
                print("HaruHaru")
                sys.exit()
            q.append((dx, dy, graph[dx][dy]))

print("Hing")
