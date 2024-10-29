import sys
from bisect import bisect_left
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

lis = [li[0]]

for i in li:
    if lis[-1] < i:
        lis.append(i)
    else:
        idx = bisect_left(lis, i)
        lis[idx] = i

print(n-len(lis))

