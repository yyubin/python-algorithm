import sys
from collections import defaultdict

n = int(sys.stdin.readline())
books = [sys.stdin.readline().rstrip() for _ in range(n)]

dic = defaultdict(int)
for i in books:
    dic[i] += 1

dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
print(dic[0][0])
