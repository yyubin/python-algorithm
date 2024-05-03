import sys
from itertools import permutations
n = int(sys.stdin.readline())
li = [i+1 for i in range(n)]
k = list(map(int, sys.stdin.readline().split()))

num = k.pop(0)

if num == 1:
    for per in permutations(li, n):
        
        if k[0] == 1:
            print(*list(per))
            sys.exit()
        k[0] -= 1

else:
    idx = 1
    for per in permutations(li, n):
        if per == tuple(k):
            print(idx)
            sys.exit()
        idx += 1
