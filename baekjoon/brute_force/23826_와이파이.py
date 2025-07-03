import sys
n = int(sys.stdin.readline())
x0, y0, e0 = map(int, sys.stdin.readline().split())
rooms = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

res = 0
for i, v in enumerate(rooms):
    x, y, e = v[0], v[1], v[2]
    public = max(e0 - (abs(x0 - x) + abs(y0 - y)), 0)
    for j, w in enumerate(rooms):
        xx, yy, ee = w[0], w[1], w[2]
        if ee > 0:
            tmp = max(ee - (abs(x-xx) + abs(y-yy)), 0)
            public -= tmp
    res = max(res, public)
print(res if res > 0 else "IMPOSSIBLE")