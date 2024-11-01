import sys
from bisect import bisect_left
for i in range(int(sys.stdin.readline())):
    n, k = map(int, sys.stdin.readline().split())
    li = list(map(int, sys.stdin.readline().split()))

    lis = [li[0]]

    for j in li:
        if lis[-1] < j:
            lis.append(j)
        else:
            idx = bisect_left(lis, j)
            lis[idx] = j

    print(f'Case #{i+1}')
    print(1 if len(lis) >= k else 0)

