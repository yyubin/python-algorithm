import sys
n, k = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

diff = [0] * (n-1)
for i in range(n-1):
    diff[i] = li[i+1] - li[i]

diff.sort()
print(sum(diff[:n-k]))


