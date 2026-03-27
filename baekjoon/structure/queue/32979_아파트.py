import sys
from collections import deque

n = int(sys.stdin.readline())
t = int(sys.stdin.readline())
a = deque(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

for i in range(t):
    for j in range(b[i]-1):
        a.append(a.popleft())

    print(a[0], end=' ')
