import sys
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    result = []
    stickers = []
    for _ in range(2):
        stickers.append(list(map(int, sys.stdin.readline().split())))

    if len(stickers[0]) == 1:
        result.append(max(stickers[0][0], stickers[1][0]))
    else:
        stickers[0][1] += stickers[1][0]
        stickers[1][1] += stickers[0][0]
        for i in range(2, n):
            stickers[0][i] += max(stickers[1][i-1], stickers[1][i-2])
            stickers[1][i] += max(stickers[0][i-1], stickers[0][i-2])
        result.append(max(stickers[0][n-1], stickers[1][n-1]))

    print(result[0])

# 대각선
# 1 2 3 4 5
# 6 7 8 9 10
# 1 선택시 1 7 3 9 5
# 2 선택시 6 2 8 4 10

# stickers[0][1] 에 대각선 stickers[1][0] 더하기
# stickers[1][1] 에 대각선 stickers[0][0] 더하기

# stickers[0][i] 에 대각선 전, 이전 값 중 더 큰 값 더해주기
# 진행후 stickers[0][n-1]과 stickers[1][n-1] 큰값
