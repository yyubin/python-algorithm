import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

li = set(li)
li = list(li)
li.sort()

print(*li)
