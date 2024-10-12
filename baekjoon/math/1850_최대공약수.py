import sys
from math import gcd
a, b = map(int, sys.stdin.readline().split())
print(gcd(a, b) * "1")
