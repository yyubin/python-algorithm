import sys
n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

li.append(0)
left = 0
right = 1
ans = 0
while left <= right < n+1:
    r = sum(li[left:right])
    if r == m:
        ans += 1
        right += 1
        left += 1
        continue

    if r < m:
        right += 1
    else:
        left += 1

print(ans)

