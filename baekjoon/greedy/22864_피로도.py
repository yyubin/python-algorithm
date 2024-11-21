import sys
a, b, c, d = map(int, sys.stdin.readline().split())
t = 24
now = 0
work = 0
while t > 0:
    t -= 1
    if now + a > d:
        now -= c
        if now < 0:
            now = 0
    else:
        now += a
        work += b
print(work)





