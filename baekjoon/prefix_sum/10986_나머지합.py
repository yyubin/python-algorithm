import sys
n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
p = [0] * (n+1)

count = [0] * (m+1)

for i in range(n):
    p[i+1] = (p[i] + li[i]) % m
    count[p[i+1]] += 1

ans = count[0]

for i in range(m+1):
    ans += (count[i] * (count[i] - 1)) // 2

print(ans)
