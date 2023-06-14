import collections
import sys
from collections import deque
from itertools import combinations


def bfs(li):
    start = li[0]
    q = deque()
    q.append(start)
    visited = {start}
    ans = 0

    while q:
        now = q.popleft()
        ans += population[now]
        for k in graph[now]:
            if k not in visited and k in li:
                q.append(k)
                visited.add(k)

    return ans, len(visited)


n = int(sys.stdin.readline())
population = list(map(int, sys.stdin.readline().split()))
graph = collections.defaultdict(list)
result = sys.maxsize

for i in range(n):
    _, *tmp = list(map(int, sys.stdin.readline().split()))
    for j in tmp:
        graph[i].append(j - 1)

for i in range(1, n // 2 + 1):
    combs = list(combinations(range(n), i))
    for comb in combs:
        re1, v1 = bfs(comb)
        re2, v2 = bfs([i for i in range(n) if i not in comb])
        if v1 + v2 == n:
            result = min(result, abs(re1 - re2))

print(-1 if result == sys.maxsize else result)

## combination으로 선거구 조합 후 bfs로 인접한 지 확인


# import sys
# from collections import deque
#
# n = int(sys.stdin.readline())
# population = list(map(int, sys.stdin.readline().split()))
# graph = [[] for _ in range(n)]
# val = sys.maxsize
#
# for i in range(n):
#     _, *tmp = list(map(int, sys.stdin.readline().split()))
#     for j in tmp:
#         graph[i].append(j - 1)
#
#
# def bfs(li):
#     q = deque()
#     q.append(li[0])
#     visited = [False for _ in range(n)]
#     visited[li[0]] = True
#     cnt, ans = 1, 0
#
#     while q:
#         now = q.popleft()
#         ans += population[now]
#         for k in graph[now]:
#             if not visited[k] and k in li:
#                 q.append(k)
#                 cnt += 1
#                 visited[k] = True
#
#     if cnt == len(li):
#         return ans
#     else:
#         return False
#
#
# def dfs(cnt, x, end):
#     global val
#     if cnt == end:
#         li1, li2 = deque(), deque()
#
#         for i in range(n):
#             if check[i]:
#                 li1.append(i)
#             else:
#                 li2.append(i)
#
#         ans1 = bfs(li1)
#         if not ans1:
#             return
#
#         ans2 = bfs(li2)
#         if not ans2:
#             return
#
#         val = min(val, abs(ans1 - ans2))
#         return
#
#     for i in range(x, n):
#         if check[i]:
#             continue
#         check[i] = True
#         dfs(cnt + 1, i, end)
#
#         check[i] = False
#
#
# for i in range(1, n // 2 + 1):
#     check = [False for _ in range(n)]
#     dfs(0, 0, i)
#
# print(-1 if val == sys.maxsize else val)
#
# ## dfs로 구 조합 만들고 bfs로 인접한지 확인
#
