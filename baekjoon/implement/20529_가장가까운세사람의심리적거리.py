from itertools import combinations
import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    li = list(map(str, sys.stdin.readline().split()))
    min_ = sys.maxsize
    if len(li) > 32:
        print(0)
        continue
    for cb1, cb2, cb3 in combinations(li, 3):
        tmp = 0
        tmp += len(set(cb1) - set(cb2))
        tmp += len(set(cb2) - set(cb3))
        tmp += len(set(cb1) - set(cb3))
        min_ = min(min_, tmp)

    print(min_)
