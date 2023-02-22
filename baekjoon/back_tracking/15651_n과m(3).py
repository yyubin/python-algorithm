import sys
import itertools
n, m = map(int, sys.stdin.readline().split())
for i in itertools.product([i+1 for i in range(n)], repeat=m):
    print(*i)
