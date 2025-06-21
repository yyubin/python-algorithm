import sys
for _ in range(int(sys.stdin.readline())):
    n, x = map(int, sys.stdin.readline().rstrip().split())
    res = list(range(n))
    if x in res:
        res.remove(x)
        res.append(x)
    print(*res)

