import sys
n = int(sys.stdin.readline())
paper = [[0]*100 for _ in range(100)]

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())

    for i in range(x-1, x+9):
        for j in range(y-1, y+9):
            paper[i][j] = 1

result = 0

for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            result += 1

print(result)
