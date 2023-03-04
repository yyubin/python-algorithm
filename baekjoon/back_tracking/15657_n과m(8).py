import sys
from itertools import combinations_with_replacement

n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
li.sort()

for i in combinations_with_replacement(li, m):
    print(*i)

