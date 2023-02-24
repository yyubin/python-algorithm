import sys
n = int(sys.stdin.readline())
li = []
d = [0] * 10000

for _ in range(n):
    li.append(int(sys.stdin.readline()))

d[0] = li[0]
if n > 1:
    d[1] = d[0] + li[1]
if n > 2:
    d[2] = max(li[2] + li[0], li[2] + li[1], d[1])
for i in range(3, n):
    d[i] = max(d[i-1], li[i] + d[i-2], li[i] + li[i-1] + d[i-3])
    #유지할지, 지금잔 마시고 이전잔은 마시지 않기, 지금잔 마시고 이전잔도 마시고 2번째 전잔은 마시지 않기

print(max(d))
