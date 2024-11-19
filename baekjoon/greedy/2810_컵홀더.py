import sys
n = int(sys.stdin.readline())
chair = list(sys.stdin.readline().rstrip())

cnt = 1
for i in range(n):
    if chair[i] == 'S':
        cnt += 1
    elif chair[i] == 'L' and chair[i-1] == 'L':
        chair[i] = 0
        cnt += 1

print(n if cnt >= n else cnt)

