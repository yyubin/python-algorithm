for _ in range(10):
    tc = int(input())
    graph = [list(map(int, input().split())) for _ in range(100)]

    a, b = 0, 0
    tmp_a, tmp_b = 0, 0
    for i in range(100):
        a = max(a, sum(graph[i]))
        tmp_li = [graph[x][i] for x in range(100)]
        b = max(b, sum(tmp_li))
        for j in range(100):
            if i == j:
                tmp_a += graph[i][j]
                tmp_b += graph[9-i][j]

    c = max(tmp_a, tmp_b)

    print(f'#{tc} {max(a, b, c)}')

