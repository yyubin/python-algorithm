import sys
from bisect import bisect_left

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    li = [int(sys.stdin.readline()) for _ in range(n)]

    lis = [li[0]]

    for i in li:
        if lis[-1] < i:
            lis.append(i)
        else:
            idx = bisect_left(lis, i)
            lis[idx] = i


    print(len(lis))

