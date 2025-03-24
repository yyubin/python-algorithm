import sys
n = int(sys.stdin.readline())
li = [sys.stdin.readline().rstrip() for _ in range(n)]

k = len(li[0])

for i in range(k-1, -1, -1):
    s = set()
    for j in li:
        s.add(j[i:])
    if len(s) == n:
        print(k-i)
        sys.exit()
print(k)
