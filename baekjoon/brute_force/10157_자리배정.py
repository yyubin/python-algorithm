import sys
c, r = map(int, sys.stdin.readline().rstrip().split())
seat = int(sys.stdin.readline())

if seat > c*r:
    print(0)
    exit()

graph = [[0]*c for _ in range(r)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

dd = x = y = 0

for i in range(1, c*r+1):
    if i == seat:
        print(y+1, x+1)
        break
    else:
        graph[x][y] = i
        x += dx[dd]
        y += dy[dd]

        if x < 0 or y < 0 or x >= r or y >= c or graph[x][y]:
            x -= dx[dd]
            y -= dy[dd]
            dd = (dd+1) % 4
            x += dx[dd]
            y += dy[dd]

        print(y, x)