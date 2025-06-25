import sys
from collections import deque
n = int(sys.stdin.readline())
switch = list(map(int, sys.stdin.readline().split()))

start = 0
for i in range(n):
    if switch[i]:
        start |= (1 << i)

change = [0] * n
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    change[i] |= (1 << i)
    for j in tmp[1:]:
        change[i] |= (1 << (j - 1))

dist = [-1] * (1 << n)
dist[start] = 0
q = deque([start])

while q:
    now = q.popleft()
    for i in range(n):
        if now & (1 << i):
            continue
        next = now ^ change[i]
        if dist[next] == -1:
            dist[next] = dist[now] + 1
            q.append(next)

print(dist[(1 << n) - 1])

# 미리 토글 상태 전부 저장해두고 xor만 하기
# dist로 몇번 눌렀는지 기록하면서 최적화
# 최적화 하는건 보고 풂

# 아래 2740ms -> 최적화 후 728ms..........

#
# toggle = [[] for _ in range(n)]
# for i in range(n):
#     tmp = list(map(int, sys.stdin.readline().split()))
#     for j in tmp[1:]:
#         toggle[i].append(j-1)
#     toggle[i].append(i)
#
# if sum(switch) == n:
#     print(0)
#     sys.exit()
#
# bit = 0
# for i in range(n):
#     if switch[i] == 1:
#         bit |= 1 << i
#
# def bfs(start):
#     visited = [False] * (1 << n)
#     q = deque([(start, 0)])
#     full = (1 << n) - 1
#
#     while q:
#         now, cnt = q.popleft()
#         if now == full:
#             return cnt
#         if visited[now]:
#             continue
#         visited[now] = True
#         for i in range(n):
#             if (now >> i) & 1 == 0:
#                 tmp = now
#                 for j in toggle[i]:
#                     tmp ^= (1 << j)
#                 q.append((tmp, cnt + 1))
#     return -1
#
# print(bfs(bit))


# s에다 같은 사이클은 무시하고 넣는구조로..
# set말고 걍 배열 쓰면 더 빠름
# 역방향에서 정방향으로 바꿈