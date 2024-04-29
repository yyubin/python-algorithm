def dfs(x, cnt):
    global result
    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            dfs(i, cnt + 1)
            visited[i] = False

    result = max(result, cnt)


for tc in range(int(input())):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    visited = [False] * (n + 1)
    result = 0

    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, n + 1):
        visited[i] = True
        dfs(i, 1)
        visited[i] = False

    print('#' + str(tc + 1), result)
