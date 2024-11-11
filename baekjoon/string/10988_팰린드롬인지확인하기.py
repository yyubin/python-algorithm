import sys
s = sys.stdin.readline().rstrip()
print(1 if s == s[::-1] else 0)