import sys
n = int(sys.stdin.readline())
a = int(sys.stdin.readline())

graph = [[0] * n for _ in range(n)]
x, y = 0, 0
val = n ** 2
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
now_dir = 0

nx, ny = 0, 0

while val > 0:
    graph[x][y] = val

    if val == a:
        nx, ny = x, y

    val -= 1

    if 0 <= x + direction[now_dir][0] < n and 0 <= y + direction[now_dir][1] < n and graph[x + direction[now_dir][0]][y + direction[now_dir][1]] == 0:
        pass
    else:
        now_dir = (now_dir + 1) % 4

    x += direction[now_dir][0]
    y += direction[now_dir][1]

for i in graph:
    print(*i)

print(nx+1, ny+1)






