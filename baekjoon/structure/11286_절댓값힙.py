import sys
import heapq

cnt = int(sys.stdin.readline())
heap = []

for _ in range(cnt):
    num = int(sys.stdin.readline().rstrip())

    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])

