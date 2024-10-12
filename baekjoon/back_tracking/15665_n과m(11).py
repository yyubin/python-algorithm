import sys
from itertools import product

n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
li.sort()
pers = []

for per in product(li, repeat=m):
    pers.append(per)

ans = sorted(list(set(pers)))

for i in ans:
    print(*i)
