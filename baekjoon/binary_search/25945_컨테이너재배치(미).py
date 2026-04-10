import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

start = 0
end = 1e9
result = 1e9

while start <= end:
    mid = (start + end) // 2

    print(mid)
    over = 0
    minus = 0

    for i in li:
        minus += (mid - i) if mid > i else 0
        over += (i - mid) if i > mid else 0

    print(mid, over, minus)

    if (0 < over - minus < n) or (0 < minus - over < n):
        result = min(result, minus)
        end = mid - 1
        print(mid, over, minus)
        continue

    if over + n - 1 < minus:
        end = mid - 1
    if over > minus + n - 1:
        start = mid + 1
    else:
        end = mid - 1


print(result)