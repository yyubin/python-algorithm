import sys
dic = dict()
for _ in range(int(sys.stdin.readline())):
    name, status = map(str, sys.stdin.readline().rstrip().split())
    dic[name] = status

ans = []
for k, v in dic.items():
    if v == 'enter':
        ans.append(k)

ans.sort(reverse=True)
print(*ans, sep="\n")
