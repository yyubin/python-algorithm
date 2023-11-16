import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
li.sort()

if sum(li) <= m:
    print(max(li))
    sys.exit()

left = 1
right = li[-1]
mid = 0

while left <= right:
    mid = (left + right) // 2
    tmp = [i if i <= mid else mid for i in li]
    sum_ = sum(tmp)

    if sum_ == m:
        print(mid)
        sys.exit()

    if sum_ < m:
        left = mid+1
    else:
        right = mid-1

print(right)

