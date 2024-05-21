import sys
n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0 or i == j == n-1:
            print(dp[n-1][n-1])
            sys.exit()

        if i+graph[i][j] < n:
            dp[i+graph[i][j]][j] += dp[i][j]

        if j+graph[i][j] < n:
            dp[i][j+graph[i][j]] += dp[i][j]



# 메모리초과
# def dfs(x, y):
#     if 0 <= x < n and 0 <= y < n:
#         dp[x][y] += 1
#         if x == y == n-1:
#             return
#         dfs(x+graph[x][y]*1, y+graph[x][y]*0)
#         dfs(x+graph[x][y]*0, y+graph[x][y]*1)
#
#
# dfs(0, 0)
# print(dp[n-1][n-1])




# 메모리 초과
# import sys
# from collections import deque
# n = int(sys.stdin.readline())
# graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# d = [(1, 0), (0, 1)]
# ans = 0
#
# def bfs(x, y):
#     global ans
#     q = deque([(x, y, graph[x][y])])
#
#     while q:
#         xx, yy, jump = q.popleft()
#         for dx, dy in d:
#             ddx = xx + (dx * jump)
#             ddy = yy + (dy * jump)
#             if 0 <= ddx < n and 0 <= ddy < n:
#                 if ddx == n-1 and ddy == n-1:
#                     ans += 1
#                 else:
#                     q.append((ddx, ddy, graph[ddx][ddy]))
#
# bfs(0, 0)
# print(ans)
