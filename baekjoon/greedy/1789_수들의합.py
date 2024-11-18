import sys
s = int(sys.stdin.readline())
now = 0
cnt = 0
if s == 1:
    print(1)
    sys.exit()

for i in range(1, s):
    if now == s:
        break
    if now > s:
        cnt -= 1
        break
    now += i
    cnt += 1

print(cnt)
