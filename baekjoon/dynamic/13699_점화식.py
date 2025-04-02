import sys
n = int(sys.stdin.readline())
if n == 0:
    print(1)
    sys.exit()
d = [0] * (n+1)
d[0] = 1
d[1] = 1
for i in range(2, n+1):
    for j in range(i):
        d[i] += d[i-j-1]*d[j]
print(d[n])

# 0일때 예외처리 빼먹음
# 잘 확인하자...
#