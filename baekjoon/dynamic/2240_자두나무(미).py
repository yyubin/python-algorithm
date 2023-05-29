import sys
t, w = map(int, sys.stdin.readline().split())
tree = []

for _ in range(t):
    tree.append(int(sys.stdin.readline()))

d = [0] * (t+1)

now = 1
for i in range(1, t):
    print(now)
    if tree[i] == now:
        d[i] = d[i-1] + 1
        continue
    if w > 0:
        if tree[i] == tree[i+1]:
            w -= 1
            d[i] = d[i-1] + 1
            now = tree[i]
    else:
        d[i] = d[i-1]

print(d[t-1])

