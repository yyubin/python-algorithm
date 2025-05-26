# 양방향 그래프가 이분 그래프라면,
# 그 그래프를 두 가지 색으로 칠할 수 있다면
# 매 턴 색이 동시에 뒤집혀도 항상 서로 다른 색에 있게 되므로 절대로 같은 정점에 도달 불가능
# 같은 색에서 출발하면
# 두 말 사이의 최단 거리는 항상 짝수, 최단 경로를 따라 움직이면 가운데에서 만남

# 1. 그래프가 이분 그래프여야 함
# 2. 두 말이 서로 다른 색에서 출발해야 함
# 이분 그래프의 두 파티션 크기를 각각 R * B 라고 했을 때 순서가 있는 쌍을 세므로 2 * R * B
# 그래프가 이분 그래프 아니면 0

# 서로 하나씩 전진하면 이분 그래프 먼저 떠올려보자..

import sys
from collections import deque
sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().strip().split())
    g[u].append(v)
    g[v].append(u)

color = [0] * (n+1)
color[1] = 1
is_bipartite = True
r_cnt, b_cnt = 0, 0
q = deque([1])

while q and is_bipartite:
    u = q.popleft()
    if color[u] == 1:
        r_cnt += 1
    else:
        b_cnt += 1
    for v in g[u]:
        if color[v] == 0:
            color[v] = -color[u]
            q.append(v)
        elif color[v] == color[u]:
            is_bipartite = False
            break

if not is_bipartite:
    print(0)
else:
    print(r_cnt * b_cnt * 2)


# 두 플레이어가 완전히 동일한 경로로 움직이게 되는 경우를 찾아야 함
# 어떤 연결 그래프에서 모든 노드가 사이클 내에 있는 컴포넌트라면,
# 두 사람이 어떻게 움직여도 같은 노드에 동시에 도달할 수 없는 경우가 발생함
# -> 트리(사이클 없는 그래프) 라면 언젠간 만남
# -> 사이클이 있으면 회전하면서 안 겹치게 도는 경우 발생
# -> 짝수 사이클에선 한 칸씩 계속 돌아가면 절대 못 만남

# 연결 요소 단위로 분리해서, 각 연결 요소가 사이클을 포함하고, 전체 노드가 사이클에 포함되는지 확인
# 이때 컴포넌트의 노드 개수를 세서 조합 계산

# 음 근데 실패

# import sys
# sys.setrecursionlimit(10 ** 6)
# n, m = map(int, sys.stdin.readline().split())
# graph = [[] for _ in range(n+1)]
#
# for _ in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# visited = [False] * (n+1)
# res = 0
#
# def dfs(u, parent):
#     global node, edge
#     visited[u] = True
#     node += 1
#     for v in graph[u]:
#         edge += 1
#         if not visited[v]:
#             dfs(v, u)
#
# for i in range(1, n+1):
#     if not visited[i]:
#         node = 0
#         edge = 0
#         dfs(i, -1)
#         edge //= 2
#         if edge >= node:
#             print(i, edge, node)
#             res += node * (node - 1)
#
# print(res)


# 경로 시뮬이 아닌 사이클 존재 여부로 풀어야 함
# 모든 쌍에 대해 bfs 시도할 시 시간 초과
# import sys
# from collections import deque
# from itertools import combinations
# n, m = map(int, sys.stdin.readline().split())
# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# def bfs(x, y):
#     q = deque()
#     q.append((x, y))
#     x_visited = [False] * (n+1)
#     x_visited[x] = True
#     y_visited = [False] * (n+1)
#     y_visited[y] = True
#
#     while q:
#         now_x, now_y = q.popleft()
#         if now_x == now_y:
#             print("reached", now_x, now_y)
#             return 0
#         for i in graph[now_x]:
#             for j in graph[now_y]:
#                 if not x_visited[i] and not y_visited[j]:
#                     x_visited[i] = True
#                     y_visited[j] = True
#                     q.append((i, j))
#     return 1
#
# res = 0
# for comb in combinations(range(1, n+1), 2):
#     print(comb)
#     res += bfs(*comb)
# print(res)