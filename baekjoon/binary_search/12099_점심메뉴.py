import sys
n, q = map(int, sys.stdin.readline().split())
li = list(tuple(map(int, sys.stdin.readline().split())) for _ in range(n))
li.sort()
qs = list(tuple(map(int, sys.stdin.readline().split())) for _ in range(q))

for u, v, x, y in qs:
    start = 0
    end = n-1
    left = 0
    right = 0

    while start <= end:
        mid = (start + end) // 2
        if li[mid][0] < u:
            start = mid + 1
        else:
            end = mid - 1
    left = start

    start = 0
    end = n-1

    while start <= end:
        mid = (start + end) // 2
        if li[mid][0] <= v:
            start = mid + 1
        else:
            end = mid - 1
    right = start

    tmp = 0
    for i in range(left, right):
        if x <= li[i][1] <= y:
            tmp += 1
    print(tmp)
