import sys
sys.setrecursionlimit(100000)
cnt = int(input())


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


while cnt > 0:
    m, n, k = map(int, sys.stdin.readline().split())

    graph = [[0 for j in range(m)] for i in range(n)]

    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        graph[b][a] = 1

    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                result += 1

    print(result)
    cnt -= 1
