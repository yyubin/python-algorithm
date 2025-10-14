import sys
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    d = [0] * 202
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        a = (a + 1) // 2
        b = (b + 1) // 2
        if a > b:
            a, b = b, a
        for i in range(a, b+1):
            d[i] += 1
    print(10 * max(d))