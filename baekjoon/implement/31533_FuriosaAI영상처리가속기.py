import sys
a = int(sys.stdin.readline())
m, n = map(int, sys.stdin.readline().split())
print(min(float(max(m/a, n)), float(max(n/a, m)), float(2*m/a), float(2*n/a)))