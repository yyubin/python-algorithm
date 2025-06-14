import sys
from collections import deque
from math import gcd
from functools import reduce

def lcm(a, b):
    return (a*b) // gcd(a, b)

def list_lcm(lst):
    return reduce(lcm, lst, 1)

def bfs(x, idx):
    q = deque([idx])
    cnt = 0
    while q:
        now = q.popleft()
        if s[now] == x and cnt > 0:
            return cnt
        else:
            q.append(p[now]-1)
            cnt += 1

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().rstrip()
    p = list(map(int, sys.stdin.readline().split()))

    cycles = []
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            cycle = []
            j = i
            while not visited[j]:
                visited[j] = True
                cycle.append(j)
                j = p[j] - 1

            origin = ''.join(s[i] for i in cycle)
            rotated = origin
            cnt = 0
            while True:
                rotated = rotated[-1] + rotated[:-1]
                cnt += 1
                if rotated == origin:
                    break
            cycles.append(cnt)

    print(list_lcm(cycles))
