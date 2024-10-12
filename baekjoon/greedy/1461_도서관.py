# 29 (to -29) + 29 (to -28)
# 11 (to 11) + 11 (to 2)
# 6 (to -6)
# 39 (-39, -37)
# 131

# 가장긴루트에 가는길에 있는 가장 먼 곳에 집을 수 있을만큼 집어서
# 마지막에 한번만 이동
# 나머지는 짝지어서 계산하면 됨

import sys

n, m = map(int, sys.stdin.readline().split())
books = list(map(int, sys.stdin.readline().split()))
result = 0
farthest = 0
plus, minus = [], []
for b in books:
    if abs(b) > abs(farthest):
        farthest = b

    if b > 0:
        plus.append(b)
    if b < 0:
        minus.append(b)

plus.sort()
minus.sort()
if farthest > 0:
    for i in range(m):
        if plus:
            plus.pop()
        else:
            break
else:
    for i in range(m):
        if minus:
            minus.pop(0)
        else:
            break

result += abs(farthest)

while plus:
    result += max(plus) * 2
    for _ in range(m):
        plus.pop()
        if not plus:
            break

while minus:
    result += abs(min(minus)) * 2
    for _ in range(m):
        minus.pop(0)
        if not minus:
            break

print(result)




