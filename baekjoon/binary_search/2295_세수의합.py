import sys
import bisect
n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]
a.sort()

s = set()
for i in range(n):
    for j in range(i, n):
        s.add(a[i] + a[j])

s = sorted(s)
res = 0

for i in range(n):
    for j in range(n):
        target = a[i] - a[j]
        idx = bisect.bisect_left(s, target)
        if idx < len(s) and target == s[idx]:
            res = max(res, a[i])

print(res)

# 2개씩 다 더해둠 -> s
# n 이중 포문에서 a[i] - a[j]가 s에 존재하는지 이분탐색
# s는 2개씩 더해둔 곳
# a[i] 가 18이고 a[j]가 8일때 8이 s에 있으면 세 개의 합이 존재한다는걸 확인 가능
# bisect는 target이 가능한 idx를 반환하므로 이게 실재 존재하는지 확인,
# 맞다면 최댓값 갱신


# for i in range(n):
#     for j in range(n):
#         s.add(a[i] + a[j])
#
# res = 0
# for i in range(n):
#     for j in s:
#         if a[i] + j in a:
#             res = max(res, a[i] + j)
#
# print(res)

# 두수 합 저장할 때 -> O(N^2)
# 세번째 값과 s의 값을 확인할 때 s의 크기가 최대 N^2 이므로 총 O(N^3)임
# 1000^3은 1,000,000,000 10억이므로 1초안에 불가

