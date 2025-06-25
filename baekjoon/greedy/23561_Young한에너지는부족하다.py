import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
li.sort()
print(li[n*2-1] - li[n])
