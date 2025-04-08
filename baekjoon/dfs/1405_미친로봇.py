import sys
n, *percentages = map(int, sys.stdin.readline().split())
direction_probs = [p / 100 for p in percentages]
visited = [[False] * 30 for _ in range(30)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = 0.0
def dfs(x, y, depth, prob):
    global ans
    if depth == n:
        ans += prob
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, prob * direction_probs[i])
            visited[nx][ny] = False


visited[14][14] = True
dfs(14, 14, 0, 1.0)
print(ans)