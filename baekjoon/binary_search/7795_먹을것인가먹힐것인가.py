import sys

def binary_search(start, li):
    left, right = 0, len(li)-1
    tmp = -1

    while left <= right:
        mid = (left + right)//2
        if li[mid] < start:
            tmp = mid
            left = mid + 1
        else:
            right = mid - 1

    return tmp+1

for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))

    b.sort()
    result = 0
    for i in range(n):
        result += binary_search(a[i], b)

    print(result)
