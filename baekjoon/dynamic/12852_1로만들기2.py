import sys
n = int(sys.stdin.readline())
d = [0] * (n+2)
v = [0] * (n+2)
li = []

d[1] = 0
v[1] = 0

def tracking(x, y):
    print(x, y, v[y])
    if x != y:
        tracking(x, v[y])
    li.append(y)

for i in range(2, n+2):
    d[i] = d[i-1] + 1
    v[i] = i-1

    if i%3 == 0 and d[i] > d[i//3] + 1:
        d[i] = d[i//3] + 1
        v[i] = i//3

    if i%2 == 0 and d[i] > d[i//2] + 1:
        d[i] = d[i//2] + 1
        v[i] = i//2

print(d[n])
print(n, end=" ")

idx = n
while v[idx] != 0:
    print(v[idx], end=" ")
    idx = v[idx]