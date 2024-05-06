for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0
    for i in range(n):
        row_li = [graph[i][x] for x in range(n)]
        row_tmp = 0
        for ii, j in enumerate(row_li):
            if j == 1:
                row_tmp += 1
            if j == 0 or ii == n-1:
                if row_tmp == m:
                    cnt += 1
                row_tmp = 0

        col_li = [graph[x][i] for x in range(n)]
        col_tmp = 0
        for ii, j in enumerate(col_li):
            if j == 1:
                col_tmp += 1
            if j == 0 or ii == n-1:
                if col_tmp == m:
                    cnt += 1
                col_tmp = 0

    print(f'#{tc} {cnt}')



