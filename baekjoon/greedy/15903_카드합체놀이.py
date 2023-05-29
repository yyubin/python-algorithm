import sys
from heapq import heappush, heappop
n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
cards = []

for card in li:
    heappush(cards, card)

for _ in range(m):
    a = heappop(cards)
    b = heappop(cards)
    heappush(cards, a+b)
    heappush(cards, a+b)

print(sum(cards))
