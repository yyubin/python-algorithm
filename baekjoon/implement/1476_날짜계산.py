import sys
e, s, m = map(int, sys.stdin.readline().split())
ans = 1

while True:
    if (ans-e) % 15 == 0 and (ans-s) % 28 == 0 and (ans-m) % 19 == 0:
        break
    ans += 1

print(ans)


# 15 28 19
# 15*n//15 + e == 28*n//28 + s == 19*n//19 + m


