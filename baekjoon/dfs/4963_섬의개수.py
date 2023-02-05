import sys


def dfs(x, y):
    global n, m
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y)  # 왼
        dfs(x + 1, y)  # 오
        dfs(x, y - 1)  # 아래
        dfs(x, y + 1)  # 위
        dfs(x+1, y+1)  # 오른쪽 위
        dfs(x+1, y-1)  # 오른쪽 아래
        dfs(x-1, y+1)  # 왼쪽 위
        dfs(x-1, y-1)  # 왼쪽 아래

        return True
    return False


while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break

    graph = [] * n
    for _ in range(m):
        graph.append(list(map(int, sys.stdin.readline().split())))

    cnt = 0
    for i in range(m):
        for j in range(n):
            if dfs(i, j):
                cnt += 1

    print(cnt)



