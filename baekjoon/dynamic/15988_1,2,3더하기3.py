import sys

tc = int(sys.stdin.readline())

d = [1, 2, 4, 7]

for _ in range(tc):
    n = int(sys.stdin.readline())
    for j in range(len(d), n):
        d.append((d[-3] + d[-2] + d[-1]) % 1000000009)

    print(d[n - 1])
