import sys
import copy
from collections import deque
from itertools import combinations
n = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().split()) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
teachers = []
empty = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'X':
            empty.append((i, j))
        if graph[i][j] == 'T':
            teachers.append((i, j))


def bfs():
    q = deque()

    for x, y in teachers:
        for u in range(4):
            q.append((x, y, u))

    while q:
        xx, yy, uu = q.popleft()

        ddx = xx + dx[uu]
        ddy = yy + dy[uu]

        if 0 <= ddx < n and 0 <= ddy < n:
            if copy_graph[ddx][ddy] == 'S':
                return False
            elif copy_graph[ddx][ddy] == 'X':
                q.append((ddx, ddy, uu))

    return True


for com in combinations(empty, 3):
    copy_graph = copy.deepcopy(graph)
    for v in com:
        copy_graph[v[0]][v[1]] = 'O'
    if bfs():
        print('YES')
        break
else:
    print('NO')

#https://pottatt0.tistory.com/entry/%EB%B0%B1%EC%A4%80-18428-%ED%95%B4%EC%84%A4-python-%EA%B0%90%EC%8B%9C-%ED%94%BC%ED%95%98%EA%B8%B0
#굳이 직접 장애물 설치하지않고 조합으로 뽑아서 bfs로 확인만 하기..
#아이디어가 안떠올랐음
