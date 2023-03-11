import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    li[i] = max(li[i], li[i-1] + li[i])

print(max(li))