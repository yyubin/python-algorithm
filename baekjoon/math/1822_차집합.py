import sys
na, nb = map(int, sys.stdin.readline().split())
a = set(map(int, sys.stdin.readline().split()))
b = set(map(int, sys.stdin.readline().split()))

res = a-b

if len(res) > 0:
    print(len(res))
    print(*sorted(list(res)))
else:
    print(0)