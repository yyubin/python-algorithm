import sys

n = int(sys.stdin.readline())
graph = []

for _ in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))

count = 0
def width():
    global count

    for k in range(n):
        cnt_row = 1
        for l in range(n - 1):
            if graph[k][l] == graph[k][l+1]:
                cnt_row += 1
                count = max(count, cnt_row)
            else:
                cnt_row = 1

def height():
    global count

    for k in range(n):
        cnt_col = 1
        for l in range(n-1):
            if graph[l][k] == graph[l+1][k]:
                cnt_col += 1
                count = max(count, cnt_col)
            else:
                cnt_col = 1

for i in range(n):
    for j in range(n - 1):
        if graph[i][j] != graph[i][j+1]:
            graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]
            width()
            height()
            graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]

        if graph[j][i] != graph[j+1][i]:
            graph[j][i], graph[j+1][i] = graph[j+1][i], graph[j][i]
            width()
            height()
            graph[j][i], graph[j+1][i] = graph[j+1][i], graph[j][i]


print(count)

## dfs로 풀어볼까 했지만 너무 x축이동 dfs, y축이동 dfs로 각각 나누고 등등 복잡해져서 포기
# 범위가 작으니 bruteforce로 풀기
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
# def xdfs(visited, x, y, tmp_graph, cnt):
#     visited[x][y] = True
#
#     for i in range(2):
#         ddx = dx[i] + x
#         ddy = dy[i] + y
#
#         if 0 <= ddx < n and 0 <= ddy < n:
#             if tmp_graph[ddx][ddy] == tmp_graph[x][y] and not tmp_graph[ddx][ddy]:
#                 cnt += 1
#                 xdfs(visited, ddx, ddy, tmp_graph, cnt)
#
#
#
# pre = graph[0][0]
# result = []
# for i in range(n):
#     for j in range(n):
#         if pre != graph[i][j]:
#             tmp_graph = copy.deepcopy(graph)
#             tmp_graph[i][j] = pre
#             visited = [[False] in range(n)]
#             cnt = 0
#
#             xdfs(visited, i, j, tmp_graph, cnt)
#             result.append(cnt)
#         pre = graph[i][j]
#
# print(result)
