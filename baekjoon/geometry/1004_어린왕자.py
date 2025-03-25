import sys
t = int(sys.stdin.readline())
for _ in range(t):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    planet_cnt = int(sys.stdin.readline())
    planets = [list(map(int, sys.stdin.readline().split())) for _ in range(planet_cnt)]
    cnt = 0
    for cx, cy, r in planets:
        flag = False
        if (x1 - cx) ** 2 + (y1 - cy) ** 2 < r ** 2:
            flag = True
            cnt += 1
        if (x2 - cx) ** 2 + (y2 - cy) ** 2 < r ** 2:
            if not flag:
                cnt += 1
            else:
                cnt -= 1
    print(cnt)

# 원에 속하는지
# 행성의 중심에서 점의 x와 y를 사용하여 대각선 길이를 구함
# 이게 반지름보다 작으면 원에 속하는 것
