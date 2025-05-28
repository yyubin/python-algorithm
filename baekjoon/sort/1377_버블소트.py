import sys
n = int(sys.stdin.readline())
li = [[int(sys.stdin.readline()), i] for i in range(n)]
li.sort()
res = 0
for i in range(n):
    _, idx = li[i]
    res = max(idx - i, res)
print(res+1)


