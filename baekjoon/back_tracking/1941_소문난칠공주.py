import sys
from collections import deque
from itertools import combinations
graph = []
positions = [(i, j) for i in range(5) for j in range(5)]
com = list(combinations(positions, 7))

for _ in range(5):
    graph.append(list(sys.stdin.readline().rstrip()))

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

result = 0

def check(comb):
    cnt = 0
    for x, y in comb:
        if graph[x][y] == 'S':
            cnt += 1
    return True if cnt >= 4 else False

def bfs(comb):
    visited = [False] * 7
    q = deque()
    q.append(comb[0])
    visited[0] = True

    while q:
        x, y = q.popleft()
        for k in range(4):
            ddx = x + dx[k]
            ddy = y + dy[k]
            if (ddx, ddy) in comb:
                idx = comb.index((ddx, ddy))
                if not visited[idx]:
                    q.append((ddx, ddy))
                    visited[idx] = True

    return False if False in visited else True

for comb in com:
    if check(comb):
        if bfs(comb):
            result += 1

print(result)



# 그냥 bfs로는 안풀림
# 25c7 을 구하는 백트래킹 문제
# 조합을 각각 구해서, 인접한지 bfs로 확인하고 s가 4개 이상이면 확인

# def bfs(x, y):
#     global result
#     visited[x][y] = True
#     tmp = []
#     q = deque()
#     q.append((x, y))
#     tmp.append(graph[x][y])
#
#     while q:
#         xx, yy = q.popleft()
#         if len(tmp) == 7:
#             cnt = 0
#             for t in tmp:
#                 if t == 'S':
#                     cnt += 1
#             if cnt >= 4:
#                 result += 1
#                 break
#             else:
#                 break
#         for k in range(4):
#             ddx = xx + dx[k]
#             ddy = yy + dy[k]
#             if 0 <= ddx < 5 and 0 <= ddy < 5 and not visited[ddx][ddy]:
#                 visited[ddx][ddy] = True
#                 tmp.append(graph[ddx][ddy])
#                 q.append((ddx, ddy))
#
# for i in range(5):
#     for j in range(5):
#         if graph[i][j] == 'S':
#             visited = [[False] * 5 for _ in range(5)]
#             bfs(i, j)
#
# print(result)

