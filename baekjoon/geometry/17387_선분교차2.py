# CCW 알고리즘 문제
# Counter Clockwise
# 점 세(p, q, r)에 대해 반시계 방향관계를 판단하는 알고리즘
# 이를 사용해 선분이 교차하는지 확인

# ccw(A, B, C) = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
# 양수 -> 점 A B C가 반시계 방향으로 진행
# 음수 -> 점 A B C가 시계 방향으로 진행
# 0 -> 세 점이 한 직선

# 두 선분이 교차하려면?
# ccw(A, B, C) * ccw(A, B, D) <= 0
# C와 D가 선분 AB에 대해 서로 다른 방향에 있어야 함
# ccw(C, D, A) * ccw(C, D, B) <= 0
# A와 B가 선분 CD에 대해 서로 다른 방향에 있어야 함

# CCW가 전부 0일경우 한 직선위에 있는 경 -> 선분이 겹치는지 확인해야함
# 두 선분이 한 직선위에 있는 경우 각 좌표의 범위가 겹치는지 확인해야 함
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
