import sys
k, l = map(int, sys.stdin.readline().split())
dic = dict()
for _ in range(l):
    i = sys.stdin.readline().rstrip()
    if i in dic:
        dic.pop(i)
    dic[i] = 0

li = list(dic.keys())
for i in range(min(len(li), k)):
    print(li[i])

# hashtable pop in -> O(1)
