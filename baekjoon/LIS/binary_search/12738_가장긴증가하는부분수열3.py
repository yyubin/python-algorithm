import sys
from bisect import bisect_left
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().rstrip().split()))

LIS = [a[0]]

for i in a:
    if LIS[-1] < i:
        LIS.append(i)
    else:
        idx = bisect_left(LIS, i)
        LIS[idx] = i

print(len(LIS))