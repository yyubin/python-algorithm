import sys
n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[[0]*n for _ in range(n)] for _ in range(3)]
dp[0][0][1] = 1 if graph[0][1] == 0 else 0

for i in range(n):
    for j in range(2, n):
        if graph[i][j] == 1:
            continue

        dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1] if graph[i][j-1] == 0 else 0
        if i > 0:
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j] if graph[i-1][j] == 0 else 0

        if i > 0 and graph[i-1][j] == 0 and graph[i][j-1] == 0 and graph[i-1][j-1] == 0:
            dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]

print(dp[0][n-1][n-1] + dp[1][n-1][n-1] + dp[2][n-1][n-1])

# 시간복잡도 O(N^2)
# N이 최대 16이므로 아주 빠르게 실행 가능
# 순회하면서 가능한 경우에 대해 전부 생각하는 것
# 최대 16이므로 bfs로도 가능할 거 같은데
# bfs로 하려면 이것도 3차원 배열로 풀어야 할듯

# import sys
# from collections import deque
# n = int(sys.stdin.readline())
# graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
# visited = [[0] * n for _ in range(n)]
#
# if graph[n-1][n-1] == 1:
#     print(0)
#     sys.exit()
#
# q = deque()
# q.append((0, 1, 1))
#
# while q:
#     x, y, prev = q.popleft()
#     if 0 <= x < n and 0 <= y < n and graph[x][y] == 0:
#         visited[x][y] += 1
#         if x != n-1 or y != n-1:
#             if prev == 1:
#                 q.append((x, y + 1, 1))
#                 q.append((x + 1, y + 1, 3))
#             if prev == 2:
#                 q.append((x + 1, y, 2))
#                 q.append((x + 1, y + 1, 3))
#             if prev == 3:
#                 if 0 <= x-1 < n and 0 <= y-1 < n and graph[x-1][y] == 0 and graph[x][y-1] == 0:
#                     q.append((x, y+1, 1))
#                     q.append((x+1, y, 2))
#                     q.append((x+1, y+1, 3))
#
#
# print(visited[n-1][n-1])
#
#
