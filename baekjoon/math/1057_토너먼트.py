import sys
n, a, b = map(int, sys.stdin.readline().split())

round = 0

while a != b:
    round += 1
    a -= a // 2
    b -= b // 2

print(round)
