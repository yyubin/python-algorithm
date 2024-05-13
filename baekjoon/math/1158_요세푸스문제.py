import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
li = [i+1 for i in range(n)]
result = []

q = deque(li)
while q:
    q.rotate(-(k-1))
    a = q.popleft()
    result.append(a)

print('<', end='')
print(*result, sep=", ", end="")
print('>')



