import sys
r, c = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'W':
            for k in range(4):
                nx = dx[k] + i
                ny = dy[k] + j
                if 0 <= nx < r and 0 <= ny < c:
                    if graph[nx][ny] == 'S':
                        print(0)
                        sys.exit()
                    elif graph[nx][ny] == '.':
                        graph[nx][ny] = 'D'

print(1)
for i in graph:
    print(*i, sep="")