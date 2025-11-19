import sys
for _ in range(int(sys.stdin.readline())):
    k, x = map(int, sys.stdin.readline().split())
    for i in range(k):
        x *= 2
    print(x)