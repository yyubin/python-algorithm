import sys
from collections import deque
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

graph = [[0] * n for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = 2

l = int(sys.stdin.readline())
dir_dic = dict()
for _ in range(l):
    x, c = sys.stdin.readline().split()
    dir_dic[int(x)] = c

time = 0
x, y = 0, 0
graph[x][y] = 1
direction = 0
def turn(a):
    global direction
    if a == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4


q = deque()
q.append((0, 0))

while True:
    time += 1
    x += dx[direction]
    y += dy[direction]

    if x < 0 or x >= n or y < 0 or y >= n:
        print(time)
        break

    if graph[x][y] == 2:
        graph[x][y] = 1
        q.append((x, y))
        if time in dir_dic:
            turn(dir_dic[time])

    elif graph[x][y] == 0:
        graph[x][y] = 1
        q.append((x, y))
        tx, ty = q.popleft()
        graph[tx][ty] = 0
        if time in dir_dic:
            turn(dir_dic[time])
    else:
        print(time)
        break


