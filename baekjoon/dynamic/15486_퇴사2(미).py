import sys
cnt = int(sys.stdin.readline())
t = []
p = []

for _ in range(cnt):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    t.append(a)
    p.append(b)

d = [0] * (cnt + 1)

for i in range(cnt):
    for j in range(t[i]+i, cnt+1):
        if d[j] < d[i] + p[i]:
            d[j] = d[i] + p[i]

print(d[-1])
