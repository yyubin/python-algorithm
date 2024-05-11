from collections import deque
def bfs(x, y):
    q = deque([(x, y, graph[x][y])])

    while q:
        xx, yy, now = q.popleft()
        for k in range(4):
            ddx = xx + dx[k]
            ddy = yy + dy[k]
            if 0 <= ddx < 4 and 0 <= ddy < 4:
                if len(now + graph[ddx][ddy]) == 7 and now + graph[ddx][ddy] not in memo:
                    memo.append(now + graph[ddx][ddy])
                elif len(now + graph[ddx][ddy]) < 7:
                    q.append((ddx, ddy, now+graph[ddx][ddy]))




for tc in range(1, int(input())+1):
    graph = [list(map(str, input().split())) for _ in range(4)]
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    visited = [[False] * 4 for _ in range(4)]
    memo = []
    for i in range(4):
        for j in range(4):
            bfs(i, j)
    print(f'#{tc} {len(memo)}')


