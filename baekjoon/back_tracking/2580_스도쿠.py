import sys
graph = []
zero = []

for _ in range(9):
    graph.append(list(map(int, sys.stdin.readline().split())))

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            zero.append((i, j))

def chk_row(n, x):
    for i in range(9):
        if graph[x][i] == n:
            return False
    return True

def chk_col(n, y):
    for i in range(9):
        if graph[i][y] == n:
            return False
    return True

def chk_rect(x, y, n):
    x = x // 3 * 3
    y = y // 3 * 3

    for i in range(3):
        for j in range(3):
            if graph[x+i][y+j] == n:
                return False

    return True

def dfs(cnt):
    if cnt == len(zero):
        for i in range(9):
            print(*graph[i])

        exit()

    x = zero[cnt][0]
    y = zero[cnt][1]

    for i in range(1, 10):
        if chk_col(i, y) and chk_rect(x, y, i) and chk_row(i, x):
            graph[x][y] = i
            dfs(cnt+1)
            graph[x][y] = 0


dfs(0)

# 어려운 로직은 아닌데 구현이 안깔끔함.....
# fail
# def fill_width(x, y):
#     li = [k+1 for k in range(9)]
#     for i, v in enumerate(graph[x]):
#         if i != y and v == 0:
#             return
#         li.remove(i)
#     graph[x][y] = li[0]
# def fill_length(x, y):
#     li = [k+1 for k in range(9)]
#     for i in range(9):
#         if graph[i][y] == 0 and i != x:
#             return
#         li.remove(graph[i][y])
#     graph[x][y] = li[0]
#
#
# def fill():
#     for i in range(9):
#         for j in range(9):
#             if graph[i][j] == 0:
#                 fill_length(i, j)
#             if graph[i][j] == 0:
#                 fill_width(i, j)
#
#     for l in graph:
#         if 0 in l:
#             fill()
#
# fill()
#
# print(graph)

