import sys
t = int(sys.stdin.readline())
def to_int(digits):
    return int(''.join(map(str, digits)))

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    x = list(map(int, sys.stdin.readline().split()))
    y = list(map(int, sys.stdin.readline().split()))
    li = list(map(int, sys.stdin.readline().split()))

    extend = li + li
    xx = to_int(x)
    yy = to_int(y)

    cnt = 0
    for i in range(n):
        z = extend[i:i+m]
        zz = to_int(z)
        if xx <= zz <= yy:
            cnt += 1
    print(cnt)