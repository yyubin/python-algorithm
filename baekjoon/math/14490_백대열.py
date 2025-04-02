import sys
import math
n, m = map(int, sys.stdin.readline().split(":"))
g = math.gcd(n, m)
print(n//g, end="")
print(":", end="")
print(m//g)