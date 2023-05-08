import sys

num = int(sys.stdin.readline())
li = []
heap = []

for _ in range(num):
    li.append(list(map(int, sys.stdin.readline().split())))

li.sort(key= lambda x: (x[1], x[0]))

l = 0
cnt = 0

for i, j in li:
    if i >= l:
        cnt += 1
        l = j

print(cnt)

