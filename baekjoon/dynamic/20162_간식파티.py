import sys
n = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(n)]
d = [0] * n
d[0] = li[0]

for i in range(1, n):
    tmp = li[i]
    for j in range(i):
        if li[j] < li[i]:
            tmp = max(tmp, li[i] + d[j])
    d[i] = tmp
print(max(d))
