import sys
from collections import defaultdict
n, d, k, c = map(int, sys.stdin.readline().split())
li = [int(sys.stdin.readline()) for _ in range(n)]
li += li

dic = defaultdict(int)
for i in li[:k]:
    dic[i] += 1
res = len(dic)
for i in range(k, len(li)//2 + k):
    dic[li[i-k]] -= 1
    if dic[li[i-k]] == 0:
        del dic[li[i-k]]
    dic[li[i]] += 1
    dic[c] = 1
    res = max(res, len(dic))
print(res)
