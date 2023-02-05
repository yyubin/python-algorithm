import sys
n, m = map(int, sys.stdin.readline().split())
dic = {}

for _ in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    dic[a] = b

li = []
for _ in range(m):
    li.append(sys.stdin.readline().rstrip())

for i in li:
    print(dic[i])
