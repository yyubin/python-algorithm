import sys
n, m = map(int, sys.stdin.readline().split())

cnt = 0

if n == 1:
    cnt = 1
elif n == 2:
    cnt = min(4, (m-1)//2 + 1)
elif m <= 6:
    cnt = min(m, 4)
else:
    cnt = m-2

print(cnt)

# import sys
# from collections import deque
#
# n, m = map(int, sys.stdin.readline().split())
# move = [(2, 1), (1, 2), (-1, 2), (-2, 1)]
# move_cnt = [0, 0, 0, 0]
#
# cnt = 0
# visited = [[False for _ in range(m)] for _ in range(n)]
#
# def bfs():
#     global cnt
#
#     x, y = 0, 0
#     q = deque()
#     q.append((x, y))
#     cnt += 1
#     visited[0][0] = True
#
#     while q:
#         xx, yy = q.popleft()
#         for i in range(4):
#             ddx = xx + move[i][1]
#             ddy = yy + move[i][0]
#
#             if cnt > 4 and move_cnt[i] > 0 and 0 in move_cnt:
#                 continue
#
#             if 0 <= ddx < m and 0 <= ddy < n and not visited[ddy][ddx]:
#                 move_cnt[i] += 1
#                 cnt += 1
#                 visited[ddy][ddx] = True
#                 q.append((ddx, ddy))
#
# bfs()
# print(cnt)
#
#
#
#
