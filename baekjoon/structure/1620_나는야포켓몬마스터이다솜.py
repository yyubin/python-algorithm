import sys

n, m = map(int, sys.stdin.readline().split())
dic = {}
rdic = {}

for i in range(n):
    dic[i + 1] = sys.stdin.readline().rstrip()

for i in range(n):
    tmp = dic.get(i+1)
    rdic[tmp] = i + 1

ans = []
for _ in range(m):
    a = input('')
    if a.isdigit():
        ans.append(dic.get(int(a)))
    else:
        ans.append(rdic.get(a))

print(*ans, sep="\n")
