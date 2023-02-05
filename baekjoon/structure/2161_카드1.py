import sys
n = int(sys.stdin.readline())
cards = [i+1 for i in range(n)]

while len(cards) != 1:
    print(cards.pop(0), end=" ")
    cards.append(cards.pop(0))

print(cards[0])




