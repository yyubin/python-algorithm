import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
li1 = deque(list(map(int, sys.stdin.readline().split())))
li2 = deque(list(map(int, sys.stdin.readline().split())))

point1 = 0
point2 = 0
result = []

while point1 < n or point2 < m:
    if point1 >= n:
        result.append(li2.popleft())
        point2 += 1
        continue
    if point2 >= m:
        result.append(li1.popleft())
        point1 += 1
        continue

    if li1[0] < li2[0]:
        result.append(li1.popleft())
        point1 += 1
    else:
        result.append(li2.popleft())
        point2 += 1

print(*result)

# 그냥 리스트끼리 더하고 sort() 써도 시간복잡도 안 벗어남..;