from collections import deque
from copy import deepcopy

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def move(board, di):
    can_merged = [[True] * n for _ in range(n)]

    if di in [0, 3]:
        start_idx, end_idx, step = 0, n, 1

    else:
        start_idx, end_idx, step = n-1, -1, -1

    for i in range(start_idx, end_idx, step):
        for j in range(start_idx, end_idx, step):
            if board[i][j] == 0:
                continue

            x, y = i, j
            value = board[x][y]
            board[x][y] = 0
            nx, ny = x + dxs[di], y + dys[di]
            while True:
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    break

                if board[nx][ny] == 0:
                    x, y = nx, ny
                    nx, ny = x + dxs[di], y + dys[di]

                elif board[nx][ny] == value and can_merged[nx][ny]:
                    x, y = nx, ny
                    can_merged[x][y] = False
                    break

                else:
                    break
            board[x][y] = board[x][y] + value

    return board

def bfs(board):
    q = deque([board])
    max_value = -1
    step = 0

    while q:
        size = len(q)

        for _ in range(size):
            board = q.popleft()

            for di in range(4):
                next_board = move(deepcopy(board), di)
                q.append(next_board)

                for i in range(n):
                    for j in range(n):
                        if next_board[i][j] > max_value:
                            max_value = next_board[i][j]      

        step += 1
        if step == 5:
            return max_value

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

print(bfs(board))


##https://dailyheumsi.tistory.com/64
