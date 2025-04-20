import sys
n, kind = map(str, sys.stdin.readline().split())
n = int(n)
s = set()
li = {'Y': 2, 'F': 3, 'O':4}

for _ in range(n):
    a = sys.stdin.readline().rstrip()
    s.add(a)

print(len(s)//(li[kind]-1))