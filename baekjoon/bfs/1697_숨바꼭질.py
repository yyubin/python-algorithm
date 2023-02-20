import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
MAX = 100001
visited = [0] * MAX

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break
        for ddx in (x-1, x+1, x*2):
            if MAX > ddx >= 0 == visited[ddx]:
                visited[ddx] = visited[x] + 1
                q.append(ddx)

bfs()


# 실패.. bfs문제였음
# cnt = 0
# while n != k:
#     if n*2 < k:
#         n *= 2
#         cnt += 1
#     elif n < k and (k - n) < (2*n - k):
#         n += 1
#         cnt += 1
#     elif n < k and (k - n) > (2*n - k):
#         n *= 2
#         cnt += 1
#     elif n > k:
#         n -= 1
#         cnt += 1
#
# print(cnt)
