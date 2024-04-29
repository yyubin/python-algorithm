from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def bfs(graph_, visited_, time_, n_):
    q = deque()
    q.append((0, 0))
    visited_[0][0] = True
    time_[0][0] = graph_[0][0]

    while q:
        now_x, now_y = q.popleft()
        for k in range(4):
            next_x = now_x + dx[k]
            next_y = now_y + dy[k]

            if 0 <= next_x < n and 0 <= next_y < n:
                if not visited_[next_x][next_y]:
                    visited_[next_x][next_y] = True
                    time_[next_x][next_y] = time_[now_x][now_y] + graph_[next_x][next_y]
                    q.append((next_x, next_y))
                else:
                    if time_[next_x][next_y] > time_[now_x][now_y] + graph_[next_x][next_y]:
                        time_[next_x][next_y] = time_[now_x][now_y] + graph_[next_x][next_y]
                        q.append((next_x, next_y))

    return time_[n_-1][n_-1]


for tc in range(int(input())):
    n = int(input())
    graph = [list(map(int, input())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    time = [[0] * n for _ in range(n)]
    ans = bfs(graph, visited, time, n)

    print('#'+str(tc+1), ans)
