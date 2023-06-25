import sys
t, w = map(int, sys.stdin.readline().split())
tree = []

for _ in range(t):
    tree.append(int(sys.stdin.readline()))

d = [[[0 for _ in range(3)] for _ in range(w+2)] for _ in range(t+1)]

if tree[0] == 1:
    d[1][0][1] = 1
else:
    d[1][1][2] = 1

for i in range(2, t+1):
    now = tree[i-1]

    for j in range(w+1):
        if now == 1:
            d[i][j][1] = max(d[i-1][j][1], d[i-1][j-1][2]) + 1
            d[i][j][2] = max(d[i-1][j][2], d[i-1][j-1][1])
        else:
            d[i][j][1] = max(d[i-1][j][1], d[i-1][j-1][2])
            d[i][j][2] = max(d[i-1][j][2], d[i-1][j-1][1]) + 1

result = 0
for v in range(w+1):
    result = max(result, d[t][v][1], d[t][v][2])

print(result)

