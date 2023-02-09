import sys
n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(li)
result = 0
while start <= end:
    mid = (start + end) // 2
    result_li = [i-mid if i-mid > 0 else 0 for i in li]
    if sum(result_li) < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
