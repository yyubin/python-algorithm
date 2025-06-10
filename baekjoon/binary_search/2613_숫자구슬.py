import sys
n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

start = 0
end = sum(li) + 1

def chk(target):
    tmp = [0 for _ in range(m)]
    group = [0 for _ in range(m)]
    now = 0
    i = 0
    while i < n and now < m:
        if tmp[now] + li[i] <= target:
            tmp[now] += li[i]
            group[now] += 1
            i += 1
        else:
            now += 1
            continue

        if n-i < m-now:
            now += 1

    if i == n and now == m:
        return True, group
    else:
        return False, group

ans = 0
ans_group = []
while start <= end:
    mid = (start + end) // 2
    tmp_res, tmp_group = chk(mid)

    if tmp_res:
        ans = mid
        ans_group = tmp_group
        end = mid - 1
    else:
        start = mid + 1

print(ans)
print(*ans_group)

# 그리디+파라메트릭서치
# 최댓값을 mid로 두고 가능한지만 확인
# ezez