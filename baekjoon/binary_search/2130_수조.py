import sys
n = int(sys.stdin.readline())
tank = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
water = int(sys.stdin.readline())

start = 0
end = 2_000_000_001
res = 2_000_000_001
eps = 1e-9

chk = 0
for b, h, w, d in tank:
    chk += h * w * d
if chk < water:
    print("OVERFLOW")
    sys.exit()

while end - start >= 1e-3:
    mid = (start + end) / 2

    tmp = 0
    for b, h, w, d in tank:
        if b < mid:
            if b + h <= mid:
                tmp += float(h * w * d)
            else:
                tmp += float((mid - b) * w * d)

    if tmp < water:
        start = mid + eps
    else:
        res = mid
        end = mid - eps

print(f"{res:.2f}")

## 실수형 이분 탐색
# end - start >= 0.001 같은 종료조건
# 오차 범위를 소수점으로 컨트롤 할 수 있어야함
# 값 갱신을 == 대신 <=, >=를 사용하여 부동소수점 비교 실수를 피해야함
# 정확한 값을 찾기보단, 소수점 몇 자리까지 좁혀가느냐가 중요함