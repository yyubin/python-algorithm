# 1325번 : 효율적인해킹
# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
#
# graph = [[] for _ in range(n + 1)]
# h = [0] * (n + 1)
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[b].append(a)
#
#
# def dfs(graph, v, visited):
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             h[i] += 1
#             dfs(graph, i, visited)
#
#
# # for i in range(1, len(graph)):
# #     visited = [False] * (n + 1)
# #     dfs(graph, i, visited)
# #     h[i] = visited.count(True)
# visited = [False] * (n + 1)
# dfs(graph, 1, visited)
# # result = [i for i, v in enumerate(h) if v == max(h)]
# print(h)
# print(*result, sep=' ')
# --> 답은 맞지만 시간초과.. bfs로 많이 푸는것 같다

# 다른사람의 dfs풀이
# BaekJoon1325.py

# import sys
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# relation = [[] for _ in range(N)]
# stack = []
# result = [0 for _ in range(N)]
#
# for _ in range(M):
#     a, b = map(int, input().split())
#     relation[b - 1].append(a - 1)
#
# for i in range(N):
#     visited = [False] * N
#     stack.append(i)
#     visited[i] = True
#
#     # dfs
#     while stack:
#         value = stack.pop()
#         result[i] += 1
#
#         length = len(relation[value])
#         for j in range(length):
#             if not visited[relation[value][j]]:
#                 stack.append(relation[value][j])
#                 visited[relation[value][j]] = True
#
# answer = []
# max_value = max(result)
# for i in range(N):
#     if result[i] == max_value:
#         print(i + 1, end=" ")

# BFS로 풀이
from collections import deque
import sys

input = sys.stdin.readline


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
h = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)


for i in range(1, len(graph)):
    visited = [False] * (n + 1)
    bfs(graph, i, visited)
    h[i] = visited.count(True)

result = [i for i, v in enumerate(h) if v == max(h)]
print(*result, sep=' ')