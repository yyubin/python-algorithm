import sys
n = int(sys.stdin.readline())
li = [0 for i in range(301)]

for i in range(n):
    li[i] = int(sys.stdin.readline())

d = [0 for i in range(301)]
d[0] = li[0]
d[1] = li[0] + li[1]
d[2] = max(li[0] + li[2], li[1] + li[2])
for i in range(3, n):
    #d[i] = max(li[i-2] + li[i-1] + d[i-3], li[i-2] + li[i] + d[i-3], li[i-1] + li[i] + d[i-3])
    d[i] = max(d[i-3] + li[i-1] + li[i], d[i-2] + li[i])
    # 마지막 전 계단 밟은 경우
    # 마지막 전 계단 밟지 않은 경우
print(d[n-1])
