import sys
from collections import Counter
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
counter = Counter(a)
cnt = 0
a.sort()

for i in range(n):
    aa = a[i]

    left = i + 1
    right = n - 1

    while left < right:
        tmp = a[left] + a[right] + aa
        if tmp == 0:
            if a[left] == a[right]:
                cnt += right - left
            else:
                cnt += counter[a[right]]
            left += 1

        elif tmp > 0:
            right -= 1
        else:
            left += 1

print(cnt)
