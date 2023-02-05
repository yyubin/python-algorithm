import itertools
import sys
sys.setrecursionlimit(10**9)

num = int(input())
per = tuple(map(int, input().split()))

li = [i+1 for i in range(num)]
nPr = list(itertools.permutations(li, num))

if per not in nPr:
    print(-1)
else:
    print(*nPr[nPr.index(per) - 1], sep=" ")
