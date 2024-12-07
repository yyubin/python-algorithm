import sys
n = int(sys.stdin.readline())
sq = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
sq.sort()
ans = 0

idx = 0
for i, s in enumerate(sq):
    if s[1] > ans:
        ans = s[1]
        idx = i

now_x, now_y = sq[0][0], sq[0][1]
for i in range(idx+1):
    if now_y < sq[i][1]:
        ans += now_y * (sq[i][0] - now_x)
        now_y = sq[i][1]
        now_x = sq[i][0]
    else:
        ans += now_y * (sq[i][0] - now_x)
        now_x = sq[i][0]

sq.sort(reverse=True)
now_x, now_y = sq[0][0], sq[0][1]
for i in range(n - (idx)):
    if now_y < sq[i][1]:
        ans += now_y * (now_x - sq[i][0])
        now_y = sq[i][1]
        now_x = sq[i][0]
    else:
        ans += now_y * (now_x - sq[i][0])
        now_x = sq[i][0]
print(ans)


