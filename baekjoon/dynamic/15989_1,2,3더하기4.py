import sys
d = [0] * 10001
d[0] = 1
for i in [1, 2, 3]:
    for j in range(i, 10001):
        d[j] += d[j-i]
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    print(d[n])