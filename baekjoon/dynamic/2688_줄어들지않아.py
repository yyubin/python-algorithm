import sys

for _ in range(int(sys.stdin.readline())):
    d = [1 for _ in range(10)]
    n = int(sys.stdin.readline())
    for i in range(n-1):
        for j in range(10):
            d[j] = sum(d[j:])

    print(sum(d))
