import sys
for _ in range(int(sys.stdin.readline())):
    n, k = map(int, sys.stdin.readline().split())
    print('1' * k + '0' * (n - k))

# adhoc
