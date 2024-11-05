import sys
n, m = map(int, sys.stdin.readline().split())
li = [int(sys.stdin.readline()) for _ in range(n)]

start = min(li)
end = sum(li)
result = 0

while start <= end:
    mid = (start + end) // 2
    tmp = 1
    money = mid
    for i in li:
        if money < i:
            tmp += 1
            money = mid
        money -= i

    if tmp > m or mid < max(li):
        start = mid + 1
    else:
        result = mid
        end = mid - 1


print(result)
