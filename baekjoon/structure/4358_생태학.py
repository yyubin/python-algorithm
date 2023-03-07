import sys
from collections import defaultdict

cnt = 0
dic = defaultdict(int)
while True:
    tmp = sys.stdin.readline().rstrip()
    if not tmp:
        break
    dic[tmp] += 1
    cnt += 1

tree = sorted(dic.items())

for name, num in tree:
    print("%s %.4f" % (name, num/cnt*100))

