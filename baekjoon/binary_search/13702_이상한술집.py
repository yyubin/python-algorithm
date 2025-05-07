import sys
n, k = map(int, sys.stdin.readline().split())
li = [int(sys.stdin.readline()) for _ in range(n)]
li.sort()
start = 1
end = li[-1]
result = 0

while start <= end:
    mid = (start + end) // 2
    res = 0
    for i in li:
        res += i // mid
    if res < k:
        end = mid - 1
    elif res > k:
        start = mid + 1
        result = max(result, mid)
    else:
        result = mid
        start = mid + 1
print(result)
