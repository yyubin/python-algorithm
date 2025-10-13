import sys
n = int(sys.stdin.readline())
mini = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
mini.sort(key=lambda x: (-x[0], x[1]))
print(mini[0][0], mini[0][1], mini[1][0], mini[1][1])
mini.sort(key=lambda x: (x[1], -x[0]))
print(mini[0][0], mini[0][1], mini[1][0], mini[1][1])