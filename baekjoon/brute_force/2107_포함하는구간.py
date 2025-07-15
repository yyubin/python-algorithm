import sys
n = int(sys.stdin.readline())
area = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    area.append((a, b))

area.sort()
res = 0
for i in range(n):
    _, y = area[i]
    cnt = 0
    for j in range(i+1, n):
        q, w = area[j]
        if y > w:
            cnt += 1
    res = max(res, cnt)
print(res)


