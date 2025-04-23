import sys
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    a = 5
    total = 0
    while a <= n:
        total += n // a
        a *= 5
    print(total)
