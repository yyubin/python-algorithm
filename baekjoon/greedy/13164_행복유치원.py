import sys
n, k = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

li.sort()

for i in range(n):
    li[i] = [li[i], -1]

group = [[] for _ in range(k)]
group[0].append(li[0][0])
li[0][1] = 0

print(li)
print(group)

tmp = []
for i in range(1, k):
    tmp.append(abs(abs(li[0][0] - li[i][0]) - abs(li[-1][0] - li[i][0])))

print(tmp)
for i in range(k-1):
    idx = tmp.index(max(tmp))
    group[i].append(li[idx][0])
    li[idx][0] = i

print(li)
print(group)

for i in range(1, n-1):
    if abs(li[i-1][0] - li[i][0]) < abs(li[i][0] - li[i+1][0]):
        group[li[i-1][1]].append(li[i][0])
        li[i][1] = li[i-1][1]

