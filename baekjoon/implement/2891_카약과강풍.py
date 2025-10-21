import sys
n, s, r = map(int, sys.stdin.readline().split())
ss = list(map(int, sys.stdin.readline().split()))
rr = list(map(int, sys.stdin.readline().split()))

li = [0] * 12
for i in ss:
    li[i] -= 1

for i in rr:
    li[i] += 1

for i in range(1, n+1):
    if li[i] == -1:
        if li[i-1] > 0:
            li[i-1] -= 1
            li[i] += 1
        elif li[i+1] > 0:
            li[i+1] -= 1
            li[i] += 1

res = 0
for i in li:
    if i == -1:
       res += 1
print(res)
