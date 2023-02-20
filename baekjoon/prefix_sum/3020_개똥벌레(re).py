import sys

n, h = map(int, sys.stdin.readline().split(" "))
side_even = [0] * h
side_odd = [0] * h
for i in range(0, n):
    k = int(sys.stdin.readline())
    if i % 2 == 0:
        side_even[k-1] += 1
    else:
        side_odd[k-1] += 1

# 종유석, 석순 따로 나눠서 누적합 계산
for i in range(h-1, 0, -1):
    side_odd[i-1] += side_odd[i]
    side_even[i-1] += side_even[i]

minn = 200001
ans = 0

for i in range(0, h):
    t = side_even[i] + side_odd[h - 1 - i]
    if t < minn:
        minn = t
        ans = 0
    if t == minn:
        ans += 1
print(minn, ans)


#https://jow1025.tistory.com/47
#https://ddggblog.tistory.com/153

#그니까 종유석의 길이가 4라고 하면 4 3 2 1 구간은 부숴야할 종유석이 한개씩 증가하고
#석순의 길이가 4라고 하면 높이가 7일 경우 7 6 5 4 구간에서 부숴야할 장애물이 하나씩 증가

