import sys

n, m = map(int, sys.stdin.readline().split())
s = set([])
l = set([])

cnt = 0
for _ in range(n):
    s.add(sys.stdin.readline().rstrip())
for _ in range(m):
    l.add(sys.stdin.readline().rstrip())

re = sorted(s & l)
print(len(re))
print(*re, sep="\n")
