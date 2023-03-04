import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
li.sort()

for i in permutations(li, m):
    print(*i)

