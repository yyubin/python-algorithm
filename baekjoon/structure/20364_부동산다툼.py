import sys
n, q = map(int, sys.stdin.readline().split())
visited = [False] * (n+1)
def chk(x):
    tmp = 0
    while x > 1:
        if visited[x]:
            tmp = x
        x = x//2
    return tmp

for _ in range(q):
    a = int(sys.stdin.readline())
    res = chk(a)
    visited[a] = True
    print(res)

