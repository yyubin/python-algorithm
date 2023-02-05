import sys
num, height = map(int, sys.stdin.readline().split())
li = []

for _ in range(num):
    li.append(int(sys.stdin.readline().strip()))

start = 1
end = max(li)

result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in li:
        if x >= mid:
            total += x // mid

    if total < height:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
