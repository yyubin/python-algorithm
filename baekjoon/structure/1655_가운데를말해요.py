import sys
import heapq

n = int(sys.stdin.readline())

left = []
right = []
for _ in range(n):
    m = int(sys.stdin.readline())

    if len(left) == len(right):
        heapq.heappush(left, -m)
    else:
        heapq.heappush(right, m)

    if right and -left[0] > right[0]:
        min_ = heapq.heappop(left)
        max_ = heapq.heappop(right)
        heapq.heappush(left, -max_)
        heapq.heappush(right, -min_)

    print(-left[0])


