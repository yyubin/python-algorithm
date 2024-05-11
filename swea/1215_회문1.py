for tc in range(1, 11):
    n = int(input())
    li = [list(map(str, input())) for _ in range(8)]
    result = 0

    for i in range(8):
        for x in range(9-n):
            rev_x = li[i][x:x+n][::-1]
            if li[i][x:x+n] == rev_x:
                result += 1
        tmp_graph = [li[j][i] for j in range(8)]
        for y in range(9-n):
            rev_y = tmp_graph[y:y+n][::-1]
            if tmp_graph[y:y+n] == rev_y:
                result += 1

    print(f'#{tc} {result}')
