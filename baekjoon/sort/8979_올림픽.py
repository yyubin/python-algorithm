import sys
n, k = map(int, sys.stdin.readline().split())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

li.sort(key=lambda x: (-x[1], -x[2], -x[3]))

idx = 0
for i in range(n):
    if k == li[i][0]:
        idx = i

for i in range(n):
    if li[idx][1:] == li[i][1:]:
        print(i+1)
        break
