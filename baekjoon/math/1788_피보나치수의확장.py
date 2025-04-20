import sys
n = int(sys.stdin.readline())
d = [0, 1]
for _ in range(2, abs(n)+1):
    d.append((d[-1] + d[-2])%1000000000)

if n > 0:
    sign = 1
elif n == 0:
    sign = 0
else:
    sign = 1 if abs(n) % 2 != 0 else -1

print(sign)
print(d[abs(n)])
