import copy
import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

possible = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            graph[i][j] = -1
        if graph[i][j] == 2:
            possible.append((i, j))

size = len(possible)
selected_combinations = []

for bitmask in range(1 << size):
    selected = []
    for i in range(size):
        if bitmask & (1 << i):
            selected.append(possible[i])

    if len(selected) == m:
        selected_combinations.append(selected)

def bfs(comb, graph):
    tmp_graph = copy.deepcopy(graph)
    visited = [[False] * n for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if tmp_graph[i][j] == 2 and (i, j) not in comb:
                tmp_graph[i][j] = 0
            if (i, j) in comb:
                visited[i][j] = True
                q.append((i, j, 0))
    while q:
        nx, ny, dist = q.popleft()
        for k in range(4):
            ddx = dx[k] + nx
            ddy = dy[k] + ny
            if 0 <= ddx < n and 0 <= ddy < n and not visited[ddx][ddy] and tmp_graph[ddx][ddy] == 0:
                visited[ddx][ddy] = True
                tmp_graph[ddx][ddy] = dist + 1
                q.append((ddx, ddy, dist + 1))

    total_dist = 0
    for i in range(n):
        for j in range(n):
            if tmp_graph[i][j] == 0:
                return -1
            if (i, j) in comb:
                total_dist = max(total_dist, 0)
                continue
            total_dist = max(total_dist, tmp_graph[i][j])


    return total_dist

res = int(1e9)
for comb in selected_combinations:
    tmp = bfs(comb, graph)
    res = res if tmp == -1 else min(res, tmp)

print(res if res != int(1e9) else -1)


## BFS 시간 복잡도 O(N^2)
# 비트마스크로 조합 구할 때 O(2^size*size)
# 최종 시간 복잡도: O(2^size * N^2)
# 바이러스 후보가 10개 이하이므로 가능
# 최대 size ≤ 15일 때 현실적으로 문제없이 실행 가능

# combination 사용시 O(N!)
# 비트마스킹 사용시 O(2^N)