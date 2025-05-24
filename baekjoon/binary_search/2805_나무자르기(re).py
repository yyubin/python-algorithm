import sys
n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
start = 0
end = max(li)
res = 0
while start <= end:
    mid = (start + end) // 2
    tmp = sum([i - mid for i in li if i - mid > 0])
    if tmp >= m:
        res = mid
        start = mid + 1
    elif tmp < m:
        end = mid - 1
print(res)