import sys
from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
cnt = 1

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = graph[x][y]

    while q:
        xx, yy = q.popleft()
        for k in range(4):
            ddx = xx + dx[k]
            ddy = yy + dy[k]
            if 0 <= ddx < n and 0 <= ddy < n:
                if visited[ddx][ddy] > visited[xx][yy] + graph[ddx][ddy]:
                    visited[ddx][ddy] = visited[xx][yy] + graph[ddx][ddy]
                    q.append((ddx, ddy))


while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    graph = []
    visited = [[sys.maxsize] * n for _ in range(n)]

    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))

    bfs(0, 0)
    print(f'Problem {cnt}: {visited[n-1][n-1]}')
    cnt += 1


# 다익스트라로 풀이 블로그
# https://bbbyung2.tistory.com/60