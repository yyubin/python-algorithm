import sys
n = int(sys.stdin.readline())
li = []
for _ in range(n):
    name, a, b, c = map(str, sys.stdin.readline().split())
    li.append((name, int(a), int(b), int(c)))

li.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in li:
    print(i[0])
