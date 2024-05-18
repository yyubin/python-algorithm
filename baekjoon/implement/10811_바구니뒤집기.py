import sys
n, m = map(int, sys.stdin.readline().split())
bucket = [i+1 for i in range(n)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    bucket[a-1:b] = bucket[a-1:b][::-1]

print(*bucket)

