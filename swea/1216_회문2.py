for _ in range(10):
    tc = int(input())
    x_graph = [list(map(str, input())) for _ in range(100)]
    y_graph = list(zip(*x_graph))
    result = 0

    for i in range(100):
        for j in range(100):
            for k in range(100):
                tmp = x_graph[i][j:k]
                if tmp == tmp[::-1]:
                    result = max(len(tmp), result)

    for i in range(100):
        for j in range(100):
            for k in range(100):
                tmp = y_graph[i][j:k]
                if tmp == tmp[::-1]:
                    result = max(len(tmp), result)

    print(f'#{tc} {result}')

## 3for for brute
