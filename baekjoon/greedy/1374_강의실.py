import heapq
import sys

num = int(sys.stdin.readline())
li = []
heap = []

for _ in range(num):
    a, b, c = map(int, sys.stdin.readline().split())
    li.append([b, c])

li.sort()

heapq.heappush(heap, li[0][1])
for i in range(1, num):
    if li[i][0] >= heap[0]:
        heapq.heappop(heap)
        heapq.heappush(heap, li[i][1])
    else:
        heapq.heappush(heap, li[i][1])
    heap.sort()

print(len(heap))

