import sys
from itertools import permutations

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

max_ = 0
for per in permutations(li):
    tmp = 0
    for i in range(len(per)-1):
        tmp += abs(per[i] - per[i+1])

    max_ = max(max_, tmp)
print(max_)
