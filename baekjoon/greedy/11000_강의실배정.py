import heapq
import sys

num = int(sys.stdin.readline())
li = []
heap = []

for _ in range(num):
    li.append(list(map(int, sys.stdin.readline().split())))

li.sort()
heapq.heappush(heap, li[0][1]) # 처음 비교할 것

for i in range(1, num): # 처음 데이터는 이미 넣었으니 1부터
    if li[i][0] >= heap[0]: # 만약 끝나는 시간이 힙에 있는 시간 보다 크면
        heapq.heappop(heap) # 강의실 사용 가능 -> 힙에서 pop
        heapq.heappush(heap, li[i][1]) # 현재 강의 끝나는 시간 넣기
    else:
        heapq.heappush(heap, li[i][1]) # 만약 아니라면 강의 끝나는 시간만 넣기

print(len(heap))
