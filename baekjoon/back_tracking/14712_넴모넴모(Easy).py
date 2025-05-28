import sys
N, M = map(int, sys.stdin.readline().split())
bbuyo = [[0] * (M + 1) for _ in range(N + 1)]
answer = 0

def dfs(cnt):
    global answer
    if cnt == N * M:
        answer += 1
        return

    y = cnt // M + 1
    x = cnt % M + 1

    dfs(cnt + 1)
    if bbuyo[y - 1][x] == 0 or bbuyo[y][x - 1] == 0 or bbuyo[y - 1][x - 1] == 0:
        bbuyo[y][x] = 1
        dfs(cnt + 1)
        bbuyo[y][x] = 0


dfs(0)
print(answer)

# 이렇게하고 pypy3로 하면 통과, 다를게 없는데 왜 ..??

# import sys
# from collections import defaultdict
# n, m = map(int, sys.stdin.readline().split())
# total = n * m
# row_mask = (1 << m) - 1
# d = [defaultdict(int) for _ in range(total+1)]
# d[0][0] = 1
#
# for i in range(total):
#     x, y = divmod(i, m)
#     last_col = (y == m - 1)
#     for mask, cnt in d[i].items():
#         prev = mask >> m
#         curr = mask & row_mask
#
#         next_curr = curr & ~(1 << y)
#         next_mask = (prev << m) | next_curr
#
#         left = (next_curr >> (y - 1)) & 1 if y > 0 else 0
#         up = (prev >> y) & 1
#         up_left = (prev >> (y - 1)) & 1 if y > 0 else 0
#         if not (left and up and up_left):
#             with_nemo = (prev << m) | (next_curr | (1 << y))
#             for nm in (next_mask, with_nemo):
#                 if last_col:
#                     nm = (nm & row_mask) << m
#                 d[i + 1][nm] += cnt
#         else:
#             nm = next_mask
#             if last_col:
#                 nm = (nm & row_mask) << m
#             d[i+1][nm] += cnt
#
# print(sum(d[total].values()))
# O(N × M × 2^M)
# 근데 이것도 시간초과
# 비트마스킹

# 왜 시간초과인지 도저히 모르겠네
# n, m <= 25잖아 이게 왜 안돼??
# 백트래킹

import sys
n, m = map(int, sys.stdin.readline().split())
graph = [[0] * (m+2) for _ in range(n+2)]
res = 0

def dfs(depth):
    global res
    if depth == n*m:
        res += 1
        return
    x = depth//m+1
    y = depth%m+1

    dfs(depth+1)

    if graph[x - 1][y] == 0 or graph[x][y - 1] == 0 or graph[x - 1][y - 1] == 0:
        graph[x][y] = 1
        dfs(depth+1)
        graph[x][y] = 0

dfs(0)
print(res)