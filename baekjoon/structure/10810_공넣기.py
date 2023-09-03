import sys
n, m = map(int, sys.stdin.readline().split())
ball = []
result = [0] * n

for _ in range(m):
    ball.append(list(map(int, sys.stdin.readline().split())))

for i in ball:
    for j in range(i[0], i[1]+1):
        result[j-1] = i[2]

print(*result)

# 3 3 0 0 0
# 3 3 4 4 0
# 1 1 1 1 0
# 1 2 1 1 0