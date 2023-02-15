from itertools import combinations
import sys

while True:
    li = list(map(int, sys.stdin.readline().split()))
    if li == [0]:
        break
    li.pop(0)
    li.sort()
    li = list(combinations(li, 6))

    for i in li:
        print(*i)
    print()
