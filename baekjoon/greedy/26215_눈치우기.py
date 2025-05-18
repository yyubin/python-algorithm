import sys
import heapq
n = int(sys.stdin.readline())
tmp = list(map(int, sys.stdin.readline().split()))
li = []
for i in range(n):
    heapq.heappush(li, -tmp[i])

cnt = 0
while len(li) > 1:
    max_ = -heapq.heappop(li)
    sec_ = -heapq.heappop(li) if li else 0

    if max_ - 1 > 0:
        heapq.heappush(li, -(max_ - 1))
    if sec_ - 1 > 0:
        heapq.heappush(li, -(sec_ - 1))
    cnt += 1

cnt += -heapq.heappop(li) if li else 0
print(cnt if cnt <= 1440 else -1)
