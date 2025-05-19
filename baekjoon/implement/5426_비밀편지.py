import math
import sys
for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().strip()
    n = len(s)
    m = int(math.sqrt(n))
    li = []
    idx = 0
    for i in range(m):
        tmp = []
        for j in range(m):
            tmp.append(s[idx])
            idx += 1
        li.append(tmp)

    res = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            res[m-j-1][i] = li[i][j]

    for i in res:
        print(*i, end="", sep="")
    print()