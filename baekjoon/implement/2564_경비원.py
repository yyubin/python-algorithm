import sys
n, m = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
li = []

for _ in range(k):
    li.append(list(map(int, sys.stdin.readline().split())))

now_dir, now_dis = map(int, sys.stdin.readline().split())
now_score = 0
if now_dir == 1:
    now_score = now_dis
elif now_dir == 2:
    now_score = (n - now_dis) + n + m
elif now_dir == 3:
    now_score = (m - now_dis) + 2*n + m
elif now_dir == 4:
    now_score = now_dis + n

result = 0
for i in range(k):
    tmp = 0
    if now_dir == li[i][0]:
        result += abs(now_dis - li[i][1])
        continue
    if li[i][0] == 1:
        tmp = li[i][1]
    elif li[i][0] == 2:
        tmp = (n - li[i][1]) + n + m
    elif li[i][0] == 3:
        tmp = (m - li[i][1]) + 2*n + m
    elif li[i][0] == 4:
        tmp = li[i][1] + n

    result += min(abs(now_score - tmp), 2*(m + n) - abs(now_score - tmp))

print(result)

# 쌩 구현문제
# 코드 줄일 수 있을 거 같지만 일단..
