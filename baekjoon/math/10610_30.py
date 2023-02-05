import sys
n = list(map(int, sys.stdin.readline().rstrip()))
result = []

if 0 not in n:
    print(-1)
else:
    n.remove(0)
    if sum(n) % 3 == 0:
        n.sort(reverse=True)
        print(*n, sep="", end="")
        print(0)
    else:
        print(-1)



