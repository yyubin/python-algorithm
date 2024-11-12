import sys
from collections import defaultdict
n = int(sys.stdin.readline())
li = [list(map(str, sys.stdin.readline().rstrip().split('.'))) for _ in range(n)]

dic = defaultdict(int)

for i in li:
    dic[i[1]] += 1
result = sorted(dic.items())
for i in result:
    print(i[0], i[1])

