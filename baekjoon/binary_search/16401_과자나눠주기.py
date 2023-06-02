import sys
m, n = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
li.sort()

left = 1
right = li[-1]

while left <= right:
    ans = (left + right) // 2
    cnt = 0
    for i in li:
        if i >= ans:
            cnt += i//ans

    if cnt >= m:
        left = ans + 1
    else:
        right = ans - 1

print(right)



