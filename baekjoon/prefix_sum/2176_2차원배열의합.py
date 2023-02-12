import sys
n, m = map(int, sys.stdin.readline().split())
li = []

for _ in range(n):
    li.append(list(map(int, sys.stdin.readline().split())))

k = int(sys.stdin.readline())

for _ in range(k):
    i, j, x, y = map(int, sys.stdin.readline().split())

    result = 0

    for a in range(i-1, x):
        for b in range(j-1, y):
            result += li[a][b]

    print(result)