import sys
from itertools import combinations
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
s = set()
for i in range(1, n+1):
    for comb in combinations(li, i):
        s.add(sum(comb))

for i in range(1, sum(li) + 2):
    if i not in s:
        print(i)
        break
