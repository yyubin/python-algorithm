import sys
a, p = map(int, sys.stdin.readline().split())
s = []
d = dict()
while True:
    if a in d:
        print(d[a])
        break
    d[a] = len(s)
    s.append(a)

    nxt = 0
    for i in str(a):
        nxt += int(i) ** p
    a = nxt

