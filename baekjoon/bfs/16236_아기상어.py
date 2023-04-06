import sys
from collections import deque

n = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

sx, sy = 0, 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            arr[i][j] = 0
            sx, sy = i, j
            break

size = 2
move_num = 0
eat = 0

while True:
    q = deque()
    q.append((sx, sy, 0))
    visited = [[False] * n for _ in range(n)]
    flag = 1e9
    fish = []
    while q:
        x, y, count = q.popleft()

        if count > flag:
            break
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] > size or visited[nx][ny]:
                    continue

                if arr[nx][ny] != 0 and arr[nx][ny] < size:
                    fish.append((nx, ny, count + 1))
                    flag = count
                visited[nx][ny] = True
                q.append((nx, ny, count + 1))

    if len(fish) > 0:
        fish.sort()
        x, y, move = fish[0][0], fish[0][1], fish[0][2]
        move_num += move
        eat += 1
        arr[x][y] = 0
        if eat == size:
            size += 1
            eat = 0
        sx, sy = x, y
    else:
        break

print(move_num)

# 예제 다 맞는데 왜 틀림?

# import sys
# from collections import deque
#
# n = int(sys.stdin.readline())
# graph = []
# dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
# shark_x, shark_y = 0, 0
#
# sharksize = 2
# eat = 0
#
# for i in range(n):
#     graph.append(list(map(int, sys.stdin.readline().split())))
#     for j in range(len(graph)):
#         if graph[i][j] == 9:
#             graph[i][j] = 0
#             shark_x, shark_y = i, j
#
#
# def find_fish(sx, sy):
#     global sharksize
#     q = deque()
#     q.append((sx, sy))
#
#     visited = [[False] * n for _ in range(n)]
#     distance = [[0] * n for _ in range(n)]
#     fishes = []
#
#     while q:
#         x, y = q.popleft()
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n:
#                 if graph[nx][ny] <= sharksize and not visited[nx][ny]:
#                     visited[nx][ny] = True
#                     distance[nx][ny] = distance[x][y] + 1
#                     q.append((nx, ny))
#
#                     if graph[nx][ny] < sharksize and graph[nx][ny] != 0:
#                         fishes.append([nx, ny, distance[nx][ny]])
#
#     fishes.sort(key=lambda a: (a[2], a[0], a[1]))
#     return fishes
#
#
# if __name__ == '__main__':
#     result = 0
#     while True:
#         fish_list = find_fish(shark_x, shark_y)
#         if len(fish_list) == 0:
#             print(result)
#             exit(0)
#
#         shark_x, shark_y, time = fish_list[0]
#         eat += 1
#
#         if sharksize == eat:
#             eat = 0
#             sharksize += 1
#
#         graph[shark_x][shark_y] = 0
#         result += time

# n = int(sys.stdin.readline())
# graph = []
# dx, dy = [0, -1, 1, 0], [1, 0, 0, -1]
# visited = [[-1] * (n+1) for _ in range(n+1)]
# baby = 2
# fishes = 0
#
# for _ in range(n):
#     li = list(map(int, sys.stdin.readline().split()))
#     graph.append(li)
#     for i in li:
#         if i not in [0, 9]:
#             fishes += 1
#
# def bfs(a, b):
#     global baby, fishes
#     same_size_cnt = 0
#     q = deque()
#     q.append((a, b))
#     graph[a][b] = 0
#     visited[a][b] = 0
#
#     while q:
#         x, y = q.popleft()
#         if fishes == 0:
#             break
#         for i in range(4):
#             nx = dx[i] + x
#             ny = dy[i] + y
#             if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] <= baby:
#                 if graph[nx][ny] != 0:
#                     fishes -= 1
#
#                 if graph[nx][ny] == baby:
#                     same_size_cnt += 1
#
#                 if same_size_cnt == baby:
#                     baby += 1
#                     same_size_cnt = 0
#
#                 q.append((nx, ny))
#                 visited[nx][ny] = visited[x][y] + 1
#                 graph[nx][ny] = 0
#             elif 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > baby:
#                 break
#
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 9:
#             bfs(i, j)
#             break
#
# result = 0
# for i in range(n):
#     for j in range(n):
#         if result < visited[i][j]:
#             result = visited[i][j]
#
# print(result)
#
