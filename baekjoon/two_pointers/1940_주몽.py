import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
li.sort()
cnt = 0
left, right = 0, n-1

while left < right:
    tmp = li[left] + li[right]
    if tmp == m:
        cnt += 1
        left += 1
        right -= 1

    if tmp > m:
        right -= 1

    if tmp < m:
        left += 1

print(cnt)



