import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

cnt = 0
a.sort()

for i in range(n):
    aa = a.pop(i)

    left = 0
    right = len(a) - 1

    while left < right:
        if a[left] + a[right] + aa == 0:
            print(a[left], a[right], aa)
            cnt += 1
            left += 1
            right -= 1
        elif a[left] + a[right] + aa > 0:
            right -= 1
        else:
            left += 1

    a.append(aa)
    a.sort()

print(cnt)
