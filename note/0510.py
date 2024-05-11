import sys

s = list(map(int, sys.stdin.readline().split()))
t = list(map(int, sys.stdin.readline().split()))

print(sum(s) if sum(s) > sum(t) else sum(t))