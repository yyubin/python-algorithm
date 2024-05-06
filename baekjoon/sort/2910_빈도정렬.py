import sys
n, c = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

dic = {}
dic_idx = 0
freq = []
for i, v in enumerate(li):
    if v not in dic:
        dic[v] = dic_idx
        dic_idx += 1

    freq.append((v, li.count(v), dic[v]))
freq.sort(key=lambda x: (-x[1], x[2]))

for i in freq:
    print(i[0], end=" ")
