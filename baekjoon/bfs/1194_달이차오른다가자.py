import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y, 0))
    visited = [[[0] * 64 for _ in range(m)] for _ in range(n)]
    visited[x][y][0] = 1

    while q:
        xx, yy, cntt = q.popleft()

        for k in range(4):
            ddx = xx + dx[k]
            ddy = yy + dy[k]

            if 0 <= ddx < n and 0 <= ddy < m and visited[ddx][ddy][cntt] == 0 and graph[ddx][ddy] != '#':

                if graph[ddx][ddy] in ['a', 'b', 'c', 'd', 'e', 'f']:
                    bit = cntt | (1 << (ord(graph[ddx][ddy]) - ord('a')))
                    if visited[ddx][ddy][bit] == 0:
                        visited[ddx][ddy][bit] = visited[xx][yy][cntt] + 1
                        q.append((ddx, ddy, bit))

                elif graph[ddx][ddy] in ['A', 'B', 'C', 'D', 'E', 'F']:
                    if cntt & (1 << (ord(graph[ddx][ddy]) - ord('A'))):
                        visited[ddx][ddy][cntt] = visited[xx][yy][cntt] + 1
                        q.append((ddx, ddy, cntt))

                elif graph[ddx][ddy] == '.':
                    visited[ddx][ddy][cntt] = visited[xx][yy][cntt] + 1
                    q.append((ddx, ddy, cntt))

                elif graph[ddx][ddy] == '1':
                    return visited[xx][yy][cntt]

    return -1


for i in range(n):
    for j in range(m):
        if graph[i][j] == '0':
            graph[i][j] = '.'
            print(bfs(i, j))
            sys.exit()



## 태그 알고 풀었는데? 헤맴
###             graph[i][j] = '.' 이거ㅓ 추가안해서 안됐던