import sys
n = int(sys.stdin.readline())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
li.sort(key=lambda x: (x[0], x[1]))
res = 0
time = 0
for i in li:
    if time < i[0]:
        time = i[0]
    time += i[1]
print(time)