import sys
x, y = map(int, sys.stdin.readline().split())

rate = (100*y) // x
left, right = 0, x
ans = x

if rate >= 99:
    print(-1)
    sys.exit()

while left <= right:
    mid = (left+right) // 2

    if (100*(y+mid)) // (x+mid) > rate:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)

### 태그까고풂
## 이분탐색이라고생각이안나네..?
