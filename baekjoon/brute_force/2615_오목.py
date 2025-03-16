import sys
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for i in range(19):
    for j in range(19):
        if graph[i][j] == 1 or graph[i][j] == 2:
            tmp = graph[i][j]

            for d in range(4):
                cnt = 1
                nx = dx[d] + i
                ny = dy[d] + j

                while 0 <= nx < 19 and 0 <= ny < 19 and graph[nx][ny] == tmp:
                    cnt += 1
                    nx += dx[d]
                    ny += dy[d]

                    if cnt > 5:
                        break

                if cnt == 5:
                    prev_x, prev_y = i - dx[d], j - dy[d]
                    next_x, next_y = i + 5 * dx[d], j + 5 * dy[d]

                    prev_ = (0 <= prev_x < 19 and 0 <= prev_y < 19 and graph[prev_x][prev_y] == tmp)
                    next_ = (0 <= next_x < 19 and 0 <= next_y < 19 and graph[next_x][next_y] == tmp)

                    if not prev_ and not next_:
                        print(tmp)
                        print(i+1, j+1)
                        sys.exit()

print(0)

# 6목 검사시 앞으로 나오는 것, 이전 것 모두 검사해야함
# 오른쪾, 아래, 오른쪽 아래, 왼쪽 아래만 검사



# 6목 검사를 단방향으로 해서 통과 x
# 로직 추가하기엔 너무 지저분해서 다시 만듦..
# import sys
# graph = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]
#
# for i in range(19):
#     for j in range(19):
#         if graph[i][j] == 1 or graph[i][j] == 2:
#             tmp = graph[i][j]
#
#             if i + 4 < 19:
#                 if all(graph[i+k][j] == tmp for k in range(5)):
#                     if i + 5 < 19:
#                         if graph[i+6][j] != tmp:
#                             print(tmp)
#                             print(i+1, j+1)
#                             sys.exit()
#                     else:
#                         print(tmp)
#                         print(i + 1, j + 1)
#                         sys.exit()
#             if j + 4 < 19:
#                 if all(graph[i][j+k] == tmp for k in range(5)):
#                     if j + 5 < 19:
#                         if graph[i][j+6] != tmp:
#                             print(tmp)
#                             print(i+1, j+1)
#                             sys.exit()
#                     else:
#                         if graph[i][j+6] != tmp:
#                             print(tmp)
#                             print(i+1, j+1)
#                             sys.exit()
#
#             if i + 4 < 19 and j + 4 < 19:
#                 for k in range(1, 5):
#                     if graph[i+k][j+k] != tmp:
#                         break
#                 else:
#                     if i + 5 < 19 and j + 5 < 19:
#                         if graph[i+6][j+6] != tmp:
#                             print(tmp)
#                             print(i+1, j+1)
#                             sys.exit()
#                     else:
#                         print(tmp)
#                         print(i + 1, j + 1)
#                         sys.exit()
#             if 0 < i - 4 < 19 and 0 < j - 4 < 19:
#                 for k in range(1, 5):
#                     if graph[i-k][j-k] != tmp:
#                         break
#                 else:
#                     if 0 < i - 5 < 19 and 0 < j - 5 < 19:
#                         if graph[i-6][j-6] != tmp:
#                             print(tmp)
#                             print(i+1, j+1)
#                             sys.exit()
#                     else:
#                         print(tmp)
#                         print(i + 1, j + 1)
#                         sys.exit()
#
# print(0)