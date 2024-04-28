# 누적합
for t in range(int(input())):
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    sum_graph = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            sum_graph[i][j] = graph[i-1][j-1] + sum_graph[i-1][j] + sum_graph[i][j-1] - sum_graph[i-1][j-1]

    result = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            tmp = sum_graph[i+m][j+m] - sum_graph[i][j+m] - sum_graph[i+m][j] + sum_graph[i][j]
            result = max(result, tmp)

    print('#'+str(t+1), result)

# 브루트포스
for t in range(int(input())):
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            tmp = graph[i:i+m][j:j+m]
            tmp_sum = 0
            for tmp_i in range(i, i+m):
                for tmp_j in range(j, j+m):
                    tmp_sum += graph[tmp_i][tmp_j]

            result = max(result, tmp_sum)

    print('#'+str(t+1), result)

