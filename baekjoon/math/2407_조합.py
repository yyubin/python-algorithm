# nCm
# n!/k!(n-k)! 와 같다
import math
import sys

n, m = map(int, sys.stdin.readline().split())
print(math.factorial(n)//(math.factorial(m)*math.factorial(n-m)))
