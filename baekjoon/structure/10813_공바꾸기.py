import sys
n, m = map(int, sys.stdin.readline().split())
li = [i+1 for i in range(n)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    li[a-1], li[b-1] = li[b-1], li[a-1]

print(*li)