import sys
n, m = map(int, sys.stdin.readline().split())
dic = dict()

for _ in range(n):
    group = sys.stdin.readline().strip()
    t = int(sys.stdin.readline())
    for _ in range(t):
        name = sys.stdin.readline().strip()
        dic[name] = group

for _ in range(m):
    tmp = sys.stdin.readline().rstrip()
    type = int(sys.stdin.readline())
    if type == 1:
        print(dic[tmp])
    else:
        names = []
        for i, v in dic.items():
            if v == tmp:
                names.append(i)
        names.sort()
        print(*names, sep='\n')
