for _ in range(10):
    tc = int(input())
    graph = [list(map(int, input().split())) for _ in range(100)]
    x, y = 99, graph[99].index(2)
    visited = [[False]*100 for _ in range(100)]

    while x != 0:
        visited[x][y] = True
        if y-1 >= 0 and graph[x][y-1] and not visited[x][y-1]:
            y -= 1
            continue
        elif y+1 < 100 and graph[x][y+1] and not visited[x][y+1]:
            y += 1
            continue
        else:
            x -= 1

    result = y

    print(f'#{tc} {result}')

