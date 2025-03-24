import sys
n = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
board = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [1, -1, 0, 1, -1, 1, 0, -1]

def find_mine(x, y):
    cnt = 0
    for k in range(8):
        nx, ny = dx[k] + x, dy[k] + y
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == '*':
                cnt += 1
    return cnt

result = [['.' for _ in range(n)] for _ in range(n)]
mine = []
flag = False

for i in range(n):
    for j in range(n):
        if graph[i][j] == "*":
            mine.append((i, j))

for i in range(n):
    for j in range(n):
        if board[i][j] == "x" and graph[i][j] == "*":
            flag = True
        if board[i][j] == "x":
            result[i][j] = find_mine(i, j)

if flag:
    for x, y in mine:
        result[x][y] = "*"

for i in result:
    print(*i, sep="")

