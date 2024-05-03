from fractions import Fraction
import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
res = []

for i in range(1, n):
    tmp = Fraction(li[0], li[i])
    res.append(f'{tmp.numerator}/{tmp.denominator}')

print(*res, sep='\n')
