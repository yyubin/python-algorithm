import sys
n = int(sys.stdin.readline())
loss = list(map(int, sys.stdin.readline().split()))
delight = list(map(int, sys.stdin.readline().split()))

d = [0] * 100

for i in range(n):
    now_c = loss[i]
    now_m = delight[i]

    for j in range(99, now_c-1, -1):
        d[j] = max(d[j], d[j-now_c] + now_m)

print(d[99])
