import sys
n = int(sys.stdin.readline())
li = [float(sys.stdin.readline()) for _ in range(n)]

ans = 0

for i in range(n):
    tmp = li[i]
    ans = max(ans, tmp)
    for j in range(i+1, n):
        tmp *= li[j]
        ans = max(ans, tmp)

print('%.3f' % ans)
