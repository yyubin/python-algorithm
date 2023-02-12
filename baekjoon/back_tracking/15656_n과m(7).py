import sys
import itertools
n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
li.sort()

nPr = itertools.product(li, repeat=m)

for i in nPr:
    print(*i)