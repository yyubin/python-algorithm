import math
import sys
a1, b1 = map(int, sys.stdin.readline().split())
a2, b2 = map(int, sys.stdin.readline().split())

c, d = a1*b2 + b1*a2, b1*b2
gcd = math.gcd(c, d)

if gcd != 1:
    c //= gcd
    d //= gcd

print(c, d)