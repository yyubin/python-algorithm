import sys
n, s = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

start = 0
end = 0
sum_ = 0
result = sys.maxsize
while True:
    if sum_ >= s:
        result = min(result, end - start)
        sum_ -= li[start]
        start += 1
    elif end == n:
        break
    else:
        sum_ += li[end]
        end += 1

print(result if result != sys.maxsize else 0)
