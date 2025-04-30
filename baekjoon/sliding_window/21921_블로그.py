import sys
n, x = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

now = sum(li[:x])
max_ = now
day = 1

for i in range(1, n-x+1):
    now -= li[i-1]
    now += li[i+(x-1)]
    if now > max_:
        day = 1
        max_ = now
    elif now == max_:
        day += 1

if max_ == 0:
    print('SAD')
else:
    print(max_)
    print(day)


#1로 시작안하면 0일때 마지막날 데이터 빼버림