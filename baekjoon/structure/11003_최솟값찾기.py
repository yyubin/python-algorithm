import sys
from collections import deque
n, l = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

q = deque()
result = []
for i in range(n):
    # index기준 이전 것들 popleft
    while q and q[0][0] <= i-l:
        q.popleft()

    # 값 최소가 아닌 것들 pop
    while q and q[-1][1] >= li[i]:
        q.pop()

    q.append((i, li[i]))
    print(q[0][1], end=" ")

