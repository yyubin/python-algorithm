# import sys
# from heapq import heappush, heappop
#
# n = int(sys.stdin.readline())
# heap = []
# while n != 0:
#     li = list(sys.stdin.readline().rstrip().split())
#     if li[0] == 'push':
#         heappush(heap, li[1])
#     elif li[0] == 'pop':
#         if len(heap) == 0:
#             print(-1)
#         else:
#             print(heappop(heap))
#     elif li[0] == 'size':
#         print(len(heap))
#     elif li[0] == 'empty':
#         if len(heap) == 0:
#             print(1)
#         else:
#             print(0)
#     elif li[0] == 'front':
#         if len(heap) == 0:
#             print(-1)
#         else:
#             print(heap[0])
#     elif li[0] == 'back':
#         if len(heap) == 0:
#             print(-1)
#         else:
#             print(heap[len(heap)-1])
#     n -= 1
#


from collections import deque
import sys
n = int(input())
deq = deque()
for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        deq.append(command[1])
    elif command[0] == 'pop':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
            deq.popleft()
    elif command[0] == 'size':
        print(len(deq))
    elif command[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif command[0] == 'back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])
