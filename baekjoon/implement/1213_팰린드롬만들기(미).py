import sys
from collections import defaultdict
li = list(sys.stdin.readline().rstrip())
dic = defaultdict(int)

for i in li:
    dic[i] += 1

string = [''] * len(li)

for i in dic:
    pass


