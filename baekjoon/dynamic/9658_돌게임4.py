import sys
n = int(sys.stdin.readline())
d = [0] * 1001

d[1] = 1
d[3] = 1
d[4] = 1
if n >= 5:
    for i in range(5, n+1):
        if not d[i-1]:
            d[i] = 1
        if not d[i-3]:
            d[i] = 1
        if not d[i-4]:
            d[i] = 1
if d[n]:
    print("SK")
else:
    print("CY")
