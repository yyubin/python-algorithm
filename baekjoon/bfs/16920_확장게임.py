import sys
from collections import deque
n, m, p = map(int, sys.stdin.readline().split())
s = [0] + list(map(int, sys.stdin.readline().split()))

player = [deque() for _ in range(p+1)]
graph = []
cnt = [0] * (p+1)
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
for _ in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))

for i in range(n):
    for j in range(m):
        if graph[i][j] != '.' and graph[i][j] != '#':
            player[int(graph[i][j])].append((i, j))
            cnt[int(graph[i][j])] += 1

def bfs():
    global moved
    moved = False
    for i in range(1, p + 1):
        if not player[i]:
            continue
        q = player[i]  # q는 플레이어 담아 둔 곳
        for _ in range(s[i]):  # 이동가능한 범위만큼 다시 반복
            if not q:
                break
            for _ in range(len(q)):
                x, y = q.popleft()
                for k in range(4):
                    ddx = dx[k] + x
                    ddy = dy[k] + y
                    if 0 <= ddx < n and 0 <= ddy < m and graph[ddx][ddy] == '.':
                        graph[ddx][ddy] = str(i)
                        q.append((ddx, ddy))
                        cnt[i] += 1
                        moved = True

moved = False
while True:
    bfs()
    if not moved:
        break

print(*cnt[1:])

#bfs풀이 출처
#https://puleugo.tistory.com/85




# bfs 실패
# import sys
# from collections import deque
# n, m, p = map(int, sys.stdin.readline().split())
# s = list(map(int, sys.stdin.readline().split()))
#
# player = deque()
# graph = []
# dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
# for _ in range(n):
#     graph.append(list(sys.stdin.readline().rstrip()))
#
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] != '.' and graph[i][j] != '#':
#             player.append((graph[i][j], i, j))
#
#
# def bfs(play, x, y):
#     global flag
#     q = deque()
#     q.append((x, y))
#     new_player = deque()
#
#     while q:
#         xx, yy = q.popleft()
#         for u in range(1, s[int(play)-1] + 1):
#             print(u)
#             for k in range(4):
#                 ddx = xx + dx[k] * u
#                 ddy = yy + dy[k] * u
#                 if 0 <= ddx < n and 0 <= ddy < m and graph[ddx][ddy] == '.':
#                     graph[ddx][ddy] = play
#                     new_player.append((play, ddx, ddy))
#                     flag = True
#
#     return new_player
#
#
# while True:
#     print(graph, sep="\n")
#     flag = False
#     new_player = deque()
#     for play, x, y in player:
#         print(play, x, y)
#         new_player += bfs(play, x, y)
#
#     if not flag:
#         break
#
#     player = new_player
#
#
# result = [0 for _ in range(p)]
# for i in graph:
#     for j in i:
#         if j != '#':
#             result[int(j)-1] += 1
#
# print(*result)


# bfs로 풀었는데 방향이 바뀌는 경우 어떻게 풀어야 할 지 모르겠음 dfs로 풀어야 할듯

