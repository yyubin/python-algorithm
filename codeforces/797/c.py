import sys
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    s = list(map(int, sys.stdin.readline().split()))
    f = list(map(int, sys.stdin.readline().split()))
    res = [f[0] - s[0]]
    time = f[0]
    for i in range(1, n):
        time = max(time, s[i])
        d = f[i] - time
        res.append(f[i] - time)
        time += d
    print(*res)

# 1:46:46