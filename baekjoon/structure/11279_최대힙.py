import sys
import heapq
n = int(sys.stdin.readline())
li = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(li) == 0:
            print(0)
        else:
            print(heapq.heappop(li) * -1)
    else:
        heapq.heappush(li, -x)
