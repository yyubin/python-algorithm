import sys
direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]
map_direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n, m = map(int, sys.stdin.readline().split())
graph = [[-1] * (m+2)]
for _ in range(n):
    tmp = [-1] + list(map(int, sys.stdin.readline().split())) + [-1]
    graph.append(tmp)
graph.append([-1] * (m+2))

n += 2
m += 2

graph_num = dict()
i, j, tmp_dir, cnt = 1, 0, 0, 2
visited = [[False] * m for _ in range(n)]
graph_num[(1, 0)] = 1
visited[0][0] = True
while True:
    if visited[i][j]:
        break
    visited[i][j] = True

    i += map_direction[tmp_dir][0]
    j += map_direction[tmp_dir][1]

    if (i == 0 and j == 0) or (i == n - 1 and j == m - 1) or (i == 0 and j == m - 1) or (i == n - 1 and j == 0):
        tmp_dir += 1
        if tmp_dir == 4:
            tmp_dir = 0
        i += map_direction[tmp_dir][0]
        j += map_direction[tmp_dir][1]

    if visited[i][j]:
        break
    graph_num[(i, j)] = cnt
    cnt += 1

def go(x, y, dir):
    while graph[x][y] != -1:
        if graph[x][y] == 1:
            if dir == 0:
                dir = 1
            elif dir == 1:
                dir = 0
            elif dir == 2:
                dir = 3
            else:
                dir = 2

        x += direction[dir][0]
        y += direction[dir][1]

        if graph[x][y] == -1:
            return x, y
    return x, y
res = []

for i in range(n):
    for j in range(m):
        if (i == 0 and j == 0) or (i == n-1 and j == m-1) or (i == 0 and j == m-1) or (i == n-1 and j == 0):
            continue
        if graph[i][j] == -1:
            tmp_x, tmp_y = i, j
            if j == 0:
                dir = 0
            elif i == n-1:
                dir = 1
            elif j == m-1:
                dir = 2
            else:
                dir = 3
            tmp_x += direction[dir][0]
            tmp_y += direction[dir][1]
            xx, yy = go(tmp_x, tmp_y, dir)
            res.append((graph_num[(i, j)], graph_num[(xx, yy)]))
res.sort()
for a, b in res:
    print(b, end=" ")





