import sys

def ccw(px, py, qx, qy, rx, ry):
    return (qx - px) * (ry - py) - (qy - py) * (rx - px)

def is_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    ccw1 = ccw(x1, y1, x2, y2, x3, y3)
    ccw2 = ccw(x1, y1, x2, y2, x4, y4)
    ccw3 = ccw(x3, y3, x4, y4, x1, y1)
    ccw4 = ccw(x3, y3, x4, y4, x2, y2)

    if ccw1 * ccw2 <= 0 and ccw3 * ccw4 <= 0:
        if ccw1 == 0 and ccw2 == 0 and ccw3 == 0 and ccw4 == 0:
            return (
                max(x1, x2) >= min(x3, x4) and max(x3, x4) >= min(x1, x2) and
                max(y1, y2) >= min(y3, y4) and max(y3, y4) >= min(y1, y2)
            )
        return True
    return False

x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())

print(1 if is_intersect(x1, y1, x2, y2, x3, y3, x4, y4) else 0)