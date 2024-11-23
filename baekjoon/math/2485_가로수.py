import sys
import math
n = int(sys.stdin.readline())
trees = [int(sys.stdin.readline()) for _ in range(n)]
gcd = trees[1] - trees[0]
for i in range(1, n-1):
    gcd = math.gcd(gcd, trees[i+1] - trees[i])

cnt = 0
for i in range(n-1):
    tmp = (trees[i+1] - trees[i])//gcd
    if tmp > 1:
        cnt += (tmp-1)

print(cnt)

