import math
import sys
from collections import defaultdict
m = int(sys.stdin.readline())
dic = defaultdict(int)

for _ in range(m):
    a, b = map(str, sys.stdin.readline().split())
    dic[a] += int(b)

for k1, i in dic.items():
    ratio = math.trunc(i * 1.618)
    for k2, j in dic.items():
        if k1 != k2 and ratio == j:
            print("Delicious!")
            sys.exit()
print("Not Delicious...")




