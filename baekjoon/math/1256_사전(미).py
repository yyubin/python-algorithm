import sys
from itertools import permutations
n, m, k = map(int, sys.stdin.readline().split())
dic = ['a'] * n + ['z'] * m
result = list(permutations(dic, len(dic)))
result.sort()

print(*result[k*len(dic) - 1], sep="")

