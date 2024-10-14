import heapq
import sys
q = []
for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(q, x)

    if x == 0:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q))