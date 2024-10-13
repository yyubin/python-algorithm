import sys

r, c, t = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

air_purifier_up = 0
air_purifier_down = 0

for x in range(r):
    if graph[x][0] == -1:
        air_purifier_up = x
        air_purifier_down = x + 1
        break


def dust_spread(li):
    new_graph = [[0 for _ in range(c)] for _ in range(r)]

    new_graph[air_purifier_up][0] = -1
    new_graph[air_purifier_down][0] = -1
    # li = (x, y, v)

    for x, y, v in li:
        cnt = 0
        dust = int(v / 5)
        for i in range(4):
            ddx = dx[i] + x
            ddy = dy[i] + y

            if 0 <= ddx < r and 0 <= ddy < c and new_graph[ddx][ddy] != -1:
                new_graph[ddx][ddy] += dust
                cnt += 1

        new_graph[x][y] += v - (dust*cnt)

    return new_graph

def fresh_up():
    dir = 0
    before = 0
    x, y = air_purifier_up, 1
    while True:
        ddx = x + up_direction[dir][0]
        ddy = y + up_direction[dir][1]

        if x == air_purifier_up and y == 0:
            break
        if ddx < 0 or ddx >= r or ddy < 0 or ddy >= c:
            dir += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x = ddx
        y = ddy

def fresh_down():
    dir = 0
    before = 0
    x, y = air_purifier_down, 1
    while True:
        ddx = x + down_direction[dir][0]
        ddy = y + down_direction[dir][1]

        if x == air_purifier_down and y == 0:
            break

        if ddx < 0 or ddx >= r or ddy < 0 or ddy >= c:
            dir += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x = ddx
        y = ddy


up_direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]
down_direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for _ in range(t):
    li = []
    for x in range(r):
        for y in range(c):
            if graph[x][y] > 0:
                li.append((x, y, graph[x][y]))

    graph = dust_spread(li)
    fresh_up()
    fresh_down()



result = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] > 0:
            result += graph[i][j]


print(result)


# 괜히 알고리즘 풀때 특히 구현할때 코드 줄일려고 하지말고 그냥 복잡하면 나눠서 코드반복해서 푸는게 빠를듯