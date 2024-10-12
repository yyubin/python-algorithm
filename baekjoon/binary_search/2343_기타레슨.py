import sys
n, m = map(int, sys.stdin.readline().split())
lecture = list(map(int, sys.stdin.readline().split()))

start = max(lecture)
end = sum(lecture)
ans = 0

while start <= end:
    mid = (start + end) // 2

    total = 0
    cnt = 1
    for i in lecture:
        if total + i > mid:
            cnt += 1
            total = 0
        total += i

    if cnt <= m:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)
