import sys
import math
n, s = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

a = [abs(s - i) for i in a]

result = a[0]
for i in a:
    result = math.gcd(i, result)

print(result)
