import sys
from collections import deque
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(a, b):
    q = deque([(a, b)])
    dist = [[sys.maxsize] * W for _ in range(H)]
    dist[a][b] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < H and 0 <= ny < W:
                if graph[nx][ny] == '*':
                    continue
                cost = 1 if graph[nx][ny] == '#' else 0
                if dist[nx][ny] > dist[x][y] + cost:
                    dist[nx][ny] = dist[x][y] + cost
                    if cost == 1:
                        q.append((nx, ny))
                    else:
                        q.appendleft((nx, ny))

    return dist

for _ in range(int(sys.stdin.readline())):
    h, w = map(int, sys.stdin.readline().split())
    H, W = h+2, w+2
    graph = [['.'] * W]
    for _ in range(h):
        graph.append(['.'] + list(sys.stdin.readline().rstrip()) + ['.'])
    graph.append(['.'] * W)

    prisoners = []
    for i in range(H):
        for j in range(W):
            if graph[i][j] == '$':
                prisoners.append((i, j))

    dist1 = bfs(0, 0)
    dist2 = bfs(prisoners[0][0], prisoners[0][1])
    dist3 = bfs(prisoners[1][0], prisoners[1][1])

    res = sys.maxsize
    for i in range(H):
        for j in range(W):
            if graph[i][j] == '*':
                continue
            total = dist1[i][j] + dist2[i][j] + dist3[i][j]
            if graph[i][j] == '#':
                total -= 2
            res = min(res, total)

    print(res)


# 세명이 만나는 지점에서의 최솟값을 구함
# 이제 #에서 만날 확률이 높은데, 이게 외부로 향하는 문이 됨
# 그리고 모든 지점에서의 각자의 dist를 더해줌
# 이때 여러명이 동시에 문을 여는거니까(상근이, 죄수1, 죄수2) -2를 해줌
# 만약 죄수 2명이 감옥내의 문을 동시에 열었어야 한다면 이때는 상근이가 감옥 안으로 들어오는 상태로 상쇄 가능
# 세 명이 협동해서 탈출하는데
# 한 명만 문을 열면 모두 통과 가능하다고 간주하는 구조

# 상근이가 밖에서 존재한다는 가정이니까 padding값 줘서 그래프 늘려야함

#
# def bfs(x, y):
#     q = deque([(x, y, 0)])
#     dist[x][y] = 1
#
#     while q:
#         x, y, cnt = q.popleft()
#         print(x, y, cnt, dist[x][y])
#         if cnt == 2:
#             return dist[x][y]
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] != "*":
#                 cost = 1 if graph[nx][ny] == "#" else 0
#                 if dist[nx][ny] > cost + dist[x][y]:
#                     dist[nx][ny] = cost + dist[x][y]
#                     tmp = 1 if graph[nx][ny] == "$" else 0
#                     if cost == 1:
#                         q.append((nx, ny, cnt + tmp))
#                     else:
#                         q.appendleft((nx, ny, cnt + tmp))
#     print(dist)
#
#
# for _ in range(int(sys.stdin.readline())):
#     h, w = map(int, sys.stdin.readline().split())
#     graph = [list(sys.stdin.readline().rstrip()) for _ in range(h)]
#     dist = [[float('inf')] * w for _ in range(h)]
#     enters = []
#     for i in range(h):
#         for j in range(w):
#             if i == 0 or j == 0:
#                 if graph[i][j] == '#':
#                     enters.append((i, j))
#
#
#     res = 0
#     for a, b in enters:
#         res = min(res, bfs(a, b))
#
#     print(res)

# 문마다 계산하는건 비효율적이라 폐기
