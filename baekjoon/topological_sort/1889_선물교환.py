import sys
from collections import deque
n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
degree = [0 for _ in range(n+1)]

for i in range(1, n+1):
    a, b = map(int, sys.stdin.readline().split())
    graph[i].extend([a, b])
    degree[a] += 1
    degree[b] += 1

q = deque()
for i in range(1, n+1):
    if degree[i] < 2:
        q.append(i)

while q:
    now = q.popleft()
    for i in graph[now]:
        degree[i] -= 1
        if degree[i] == 1:
            q.append(i)

ans = [i for i in range(1, n + 1) if degree[i] == 2]
print(len(ans))
if ans:
    print(*ans)


# 모든 노드가 out-degree 2라는걸 이용해야함
# 위상정렬은 acyclic한 그래프에 유효, 사이클 안의 노드가 정답 되는 경우라 방향성이 다름
# 사이클만 정답임

# import sys
# from collections import deque
# n = int(sys.stdin.readline())
# graph = [[] for _ in range(n+1)]
# degree = [0 for _ in range(n+1)]
#
# for i in range(1, n+1):
#     a, b = map(int, sys.stdin.readline().split())
#     degree[a] += 1
#     degree[b] += 1
#     graph[i].append(a)
#     graph[i].append(b)
#
# q = deque()
# for i in range(1, n+1):
#     if degree[i] == 0:
#         q.append(i)
#
# res = [i for i in range(1, n+1)]
# while q:
#     now = q.popleft()
#     for i in graph[now]:
#         degree[i] -= 1
#         if degree[i] == 0:
#             q.append(i)
#
#     for i in degree[1:]:
#         if i != 2 and i != 0:
#             break
#     else:
#         res.remove(now)
#
# print(degree)
# if len(res) < 1:
#     print(0)
# else:
#     print(*res)