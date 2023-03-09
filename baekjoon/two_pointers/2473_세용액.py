import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

li.sort()
x = sys.maxsize
result = []

for i in range(n-2):
    fix = li[i]

    left = i+1
    right = n-1

    while left < right:
        cur = fix + li[left] + li[right]
        if abs(cur) <= abs(x):
            result = [fix, li[left], li[right]]
            x = cur

        if cur < 0:
            left += 1
        elif cur > 0:
            right -= 1
        else:
            print(*result)
            sys.exit()

print(*result)
