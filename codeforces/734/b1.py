import sys
from collections import defaultdict
for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().strip()
    tmp = 0
    d = defaultdict(int)
    for i in s:
        if d[i] >= 2:
            continue
        d[i] += 1

    for k, v in d.items():
        tmp += v

    print(tmp//2)