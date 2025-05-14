import sys
n = int(sys.stdin.readline())
li = list(map(str, sys.stdin.readline().split()))
dic = {}
for i in li:
    if i[-6:] != "Cheese":
        continue
    if i in dic:
        dic[i] += 1
        continue
    dic[i] = 1
print('yummy' if len(dic) >= 4 else 'sad')