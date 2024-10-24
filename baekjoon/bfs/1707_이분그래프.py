import sys
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        now = q.popleft()
        for x in graph[now]:
            if visited[x] == 0:
                visited[x] = visited[now] * -1
                q.append(x)
            elif visited[x] == visited[now]:
                return False

    return True


for _ in range(int(sys.stdin.readline())):
    v, e = map(int, sys.stdin.readline().split())
    graph = [list() for _ in range(v+1)]

    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (v + 1)

    for i in range(1, v+1):
        if visited[i] == 0:
            if not bfs(i):
                print('NO')
                break
    else:
        print('YES')



## 이분그래프
# 서로 인접하지 않은 두 그룹으로 나눌수 있는그래프
# bfs로 이동하면서 색칠했을때 두가지 색이 색칠되지 않을 경우
