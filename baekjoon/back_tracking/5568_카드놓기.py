import sys
from itertools import permutations
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(n)]
s = set()

for per in permutations(li, k):
    tmp = ''
    for i in per:
        tmp += str(i)
    s.add(tmp)

print(len(s))
