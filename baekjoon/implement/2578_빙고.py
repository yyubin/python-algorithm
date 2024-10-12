import sys
bingo = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
speak = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
check = [[False] * 5 for _ in range(5)]

def check_bingo():
    result = 0

    for i in range(5):
        cnt = 0
        for j in range(5):
            if check[i][j]:
                cnt += 1

        if cnt == 5:
            result += 1

    for i in range(5):
        cnt = 0
        for j in range(5):
            if check[j][i]:
                cnt += 1

        if cnt == 5:
            result += 1

    cnt = 0
    for i in range(5):
        if check[i][i]:
            cnt += 1

    if cnt == 5:
        result += 1

    cnt = 0
    for i in range(5):
        if check[i][4-i]:
            cnt += 1

    if cnt == 5:
        result += 1

    return result


ans = 0

for a in range(5):
    for b in range(5):
        now = speak[a][b]
        ans += 1

        for x in range(5):
            for y in range(5):
                if bingo[x][y] == now:
                    check[x][y] = True

        if check_bingo() >= 3:
            print(ans)
            sys.exit()


