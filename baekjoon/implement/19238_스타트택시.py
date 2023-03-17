import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

x, y = map(int, sys.stdin.readline().split())
work = [list(map(int, input().split())) for _ in range(m)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def bfs(nx, ny):
    visited = [[-1] * n for _ in range(n)]
    q = deque()
    q.append((nx, ny))
    visited[nx][ny] = 0

    while q:
        xx, yy = q.popleft()
        for u in range(4):
            ddx = dx[u] + xx
            ddy = dy[u] + yy
            if 0 <= ddx < n and 0 <= ddy < n and visited[ddx][ddy] == -1:
                if graph[ddx][ddy] == 0:
                    q.append((ddx, ddy))
                    visited[ddx][ddy] = visited[xx][yy] + 1

    return visited

def find_min(visited, work):
    i = 0
    for a, b, c, d in work:
        work[i].append(visited[a-1][b-1])
        i += 1

    work.sort(key=lambda x: (-x[4], -x[0], -x[1]))

while work:
    visited = bfs(x-1, y-1)
    find_min(visited, work)
    a, b, c, d, dist = work.pop()

    for tmp in work:
        tmp.pop()

    visited = bfs(a-1, b-1)
    dist2 = visited[c-1][d-1]
    x, y = c, d

    if dist == -1 or dist2 == -1:
        print(-1)
        sys.exit()

    k -= dist
    if k < 0:
        break

    k -= dist2
    if k < 0:
        break

    k += dist2 * 2

if k < 0:
    print(-1)
else:
    print(k)

# 구현문제가 제일 귀찮아........

# for _ in range(len(work)):
#     idx = find_min(x, y)
#
#     for i in range(n):
#         for j in range(n):
#             if i == work[idx][0] and j == work[idx][1]:
#                 result -= bfs(x, y, i, j)
#                 if result <= 0:
#                     print(-1)
#                     sys.exit()
#                 result += 2 * bfs(i, j, work[idx][2], work[idx][3])
#                 x = i
#                 y = j
#
# print(result)
