import sys
board = [list(map(str, sys.stdin.readline())) for _ in range(8)]
cnt = 0
for i in range(8):
    for j in range(8):
        if i%2 == 1 and j%2 == 1 and board[i][j] == 'F':
            cnt += 1
        elif i%2 == 0 and j%2 == 0 and board[i][j] == 'F':
            cnt += 1

print(cnt)

