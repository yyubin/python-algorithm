import sys
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    d = dict()
    for _ in range(n):
        a, b = map(str, sys.stdin.readline().split())
        if b not in d:
            d[b] = 1
        else:
            d[b] += 1
    res = 1
    for i, v in d.items():
        res *= (v+1)
    print(res - 1)
