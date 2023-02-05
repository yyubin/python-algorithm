import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]


def div(x, y, n):
    ck = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if ck != graph[i][j]:
                print('(', end="")
                div(x, y, n // 2)
                div(x, y + n // 2, n // 2)
                div(x + n // 2, y, n // 2)
                div(x + n // 2, y + n // 2, n // 2)
                print(')', end="")
                return

    if ck == 0:
        print('0', end="")
        return
    else:
        print('1', end="")
        return


div(0, 0, n)
