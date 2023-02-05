import sys
from bisect import bisect_left, bisect_right

def bisect(arr, x, y):
    right_idx = bisect_right(arr, y)
    left_idx = bisect_left(arr, x)
    return right_idx -  left_idx


cnt = int(sys.stdin.readline())

for _ in range(cnt):

    cnt1 = int(sys.stdin.readline().rstrip())
    memo1 = list(map(int, sys.stdin.readline().rstrip().split()))

    cnt2 = int(sys.stdin.readline().rstrip())
    memo2 = list(map(int, sys.stdin.readline().rstrip().split()))

    memo1.sort()

    for i in memo2:
        if bisect(memo1, i, i) == 0:
            print(0)
        else:
            print(1)




