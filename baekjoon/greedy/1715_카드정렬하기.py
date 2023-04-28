import sys
import heapq
n = int(sys.stdin.readline())
cards = []

for _ in range(n):
    heapq.heappush(cards, int(sys.stdin.readline()))


if len(cards) == 1:
    print(0)
else:
    result = 0
    while len(cards) > 1:
        tmp1 = heapq.heappop(cards)
        tmp2 = heapq.heappop(cards)
        result += tmp1 + tmp2
        heapq.heappush(cards, tmp1 + tmp2)

    print(result)
