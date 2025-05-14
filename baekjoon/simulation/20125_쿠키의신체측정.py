import sys
n = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
heart = (0, 0)

def find(center, dir):
    x, y = center[0], center[1]
    res = 0
    while True:
        x = x + dir[0]
        y = y + dir[1]
        if 0 <= x < n and 0 <= y < n and graph[x][y] == '*':
            res += 1
        else:
            break
    return res

for i in range(n):
    for j in range(n):
        if graph[i][j] == '*':
            for k in range(4):
                ddx = dx[k] + i
                ddy = dy[k] + j
                if 0 <= ddx < n and 0 <= ddy:
                    if graph[ddx][ddy] != '*':
                        break
            else:
                heart = (i, j)

left_arm = find(heart, (0, -1))
right_arm = find(heart, (0, 1))
waist = find(heart, (1, 0))
left_leg = find((heart[0]+waist, heart[1]-1), (1, 0))
right_leg = find((heart[0]+waist, heart[1]+1), (1, 0))
print(heart[0]+1, heart[1]+1)
print(left_arm, right_arm, waist, left_leg, right_leg)


