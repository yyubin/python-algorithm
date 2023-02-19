# import heapq
# import sys
#
# n, w, l = map(int, sys.stdin.readline().rstrip().split())
# heap = []
#
# weights = list(map(int, sys.stdin.readline().rstrip().split()))
# weights = [[i, w] for i in weights]
#
# time = 0
# heapq.heappush(heap, weights[0])
# while heap:
#     for i in range(len(heap)):
#         heap[i][1] -= 1
#         if heap[i][1] == 0:
#             heapq.heappop(heap)
#     time += 1
#     for i in range(n):
#         if sum([i[0] for i in heap]) + weights[i][0] <= l and weights[i][1] != 0:
#             heapq.heappush(heap, weights[i])
#         else:
#             break
#
#
# print(time)

import sys
n, w, l = map(int, sys.stdin.readline().split())
trucks = list(map(int, sys.stdin.readline().split()))

bridge = [0] * w #다리의 칸수
time = 0

while bridge:
    time += 1 #시간은 매번 흐름
    bridge.pop(0) #다리의 칸 줄이기
    if trucks: #더 건너올 트럭이 있다면
        if sum(bridge) + trucks[0] <= l: #트럭 무게를 수용할 수 있으면
            bridge.append(trucks.pop(0)) #다리에 트럭추가
        else:
            bridge.append(0) #아니면 빈공간 추가
print(time)
