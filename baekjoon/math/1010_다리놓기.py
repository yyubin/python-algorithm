import math
import sys
for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    print(math.factorial(m) // (math.factorial(n) * math.factorial(m-n)))
