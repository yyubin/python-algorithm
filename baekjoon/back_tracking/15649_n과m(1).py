import sys
from itertools import permutations
n, m = map(int, sys.stdin.readline().split())
li = [i+1 for i in range(n)]

for i in permutations(li, m):
    print(*i)
