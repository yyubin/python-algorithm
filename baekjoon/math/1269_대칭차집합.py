import sys
an, bn = map(int, sys.stdin.readline().split())
a = set(list(map(int, sys.stdin.readline().split())))
b = set(list(map(int, sys.stdin.readline().split())))

print(len(a-b) + len(b-a))
