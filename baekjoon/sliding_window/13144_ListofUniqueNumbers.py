import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

used = [0] * 100001
start = 0
end = 0
cnt = 0

while start < n:
    while end < n and used[li[end]] == 0:
        used[li[end]] = 1
        end += 1
    cnt += (end - start)
    used[li[start]] = 0
    start += 1
print(cnt)