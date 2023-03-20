import sys
import heapq
tc = int(sys.stdin.readline())

for _ in range(tc):
    k = int(sys.stdin.readline())
    q1, q2 = [], []
    visited = [False] * k

    for i in range(k):
        com, num = sys.stdin.readline().split()

        if com == 'I':
            heapq.heappush(q1, (int(num), i))
            heapq.heappush(q2, (-int(num), i))
            visited[i] = True
        else:
            if num == '1':
                while q2 and not visited[q2[0][1]]:
                    heapq.heappop(q2)
                if q2:
                    visited[q2[0][1]] = False
                    heapq.heappop(q2)
            else:
                while q1 and not visited[q1[0][1]]:
                    heapq.heappop(q1)
                if q1:
                    visited[q1[0][1]] = False
                    heapq.heappop(q1)
    while q1 and not visited[q1[0][1]]:
        heapq.heappop(q1)
    while q2 and not visited[q2[0][1]]:
        heapq.heappop(q2)

    if not q1 or not q2:
        print('EMPTY')
    else:
        print(-q2[0][0], q1[0][0])

# 시간초과
# for _ in range(tc):
#     k = int(sys.stdin.readline())
#     q = deque()
#     for _ in range(k):
#         li = list(sys.stdin.readline().split())
#         li[1] = int(li[1])
#
#         if li[0] == 'I':
#             q.append(li[1])
#         elif li[0] == 'D':
#             if len(q) == 0:
#                 continue
#             if li[1] == 1:
#                 q.remove(max(q))
#             else:
#                 q.remove(min(q))
#     if len(q) == 0:
#         print("EMPTY")
#     else:
#         print(max(q), min(q))
