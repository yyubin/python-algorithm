import sys
sys.setrecursionlimit(10 ** 6)
n, m = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
group = [[-1] * m for _ in range(n)]
group_id = 0
dir_map = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

def dfs(x, y, trace):
    visited[x][y] = 1
    trace.append((x, y))
    dx, dy = dir_map[graph[x][y]]
    nx, ny = x + dx, y + dy

    if not visited[nx][ny]:
        dfs(nx, ny, trace)
    else:
        if group[nx][ny] == -1:
            global group_id
            while True:
                tx, ty = trace.pop()
                group[tx][ty] = group_id
                if (tx, ty) == (nx, ny):
                    break
            group_id += 1
        else:
            num = group[nx][ny]
            for xx, yy in trace:
                group[xx][yy] = num
            trace.clear()

    if group[x][y] == -1:
        group[x][y] = group[nx][ny]

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i, j, [])

print(group_id)

#각 칸은 방향이 하나이므로 각 칸은 단 하나의 이웃으로 향하는 단방향 그래프
#모든 노드는 정확히 1개의 엣지를 가지므로, 결국 모든 노드는 어떤 사이클로 향하게 되어있음
#하나의 사이클에 도달하는 모든 경로는 동일한 SAFE ZONE으로 커버 가능
#서로 다른 사이클의 개수 == 필요한 SAFE ZONE의 최소 개수

#dfs로 경로를 저장하면서 해당 방향으로 이동
#만약 처음 방문하는 곳이라면 계속 전행
#방문했던 곳이라면 사이클 종료
#해당 방문지점의 group_id가 -1이라면 처음 방문한 곳이므로 사이클이 추가됨
#group_id += 1,
#지금까지의 경로들도 저장

#방문지점의 group_id가 -1이 아니라면 기존 사이클에 편입
#지금까지의 경로들도 저장

#group_id가 사이클의 개수가 됨