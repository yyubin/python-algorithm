import sys
k = int(sys.stdin.readline())
d = [[0, 0] for _ in range(k+2)]
d[1][0] = 0
d[1][1] = 1
d[2][0] = 1
d[2][1] = 1

for i in range(3, k+1):
    d[i][0] = d[i-1][1]
    d[i][1] = d[i-1][0] + d[i-1][1]

print(*d[k], sep=" ")

# 1
# 1
# 2
# 3
# 5 BABBA (2, 3)
# 8 BABBABAB (3, 5)
# fibo
