import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
tmp = sum(li)
res = 0
for i in range(n):
    tmp -= li[i]
    res += tmp * li[i]
print(res)