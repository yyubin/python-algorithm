import sys

n = int(sys.stdin.readline())
t = list(map(int, sys.stdin.readline().split()))

t.sort(reverse=True)

time = 0
for i in range(n):
    time = max(time, i+1+t[i])

print(time+1)
