import sys
n, k = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(li)
ans = 0

def chk(mid):
    can = [1 if i <= mid else 0 for i in li]
    cant = 0
    for i in range(n):
        if can[i] == 0:
            cant += 1
        else:
            cant = 0
        if cant >= k:
            return False
    return True

while start <= end:
    mid = (start + end) // 2
    res = chk(mid)

    if res:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)

# dp인줄 알았는데
# 그냥 어떤 비용 x를 기준으로 최대 비용이 x 이하인 의뢰들만 수락할 수 있는지 판별하면
# x를 이분탐색으로 줄이면서 최솟값 찾기 가능

# 최댓값을 최소화하라 → 파라메트릭 서치의 전형 패턴