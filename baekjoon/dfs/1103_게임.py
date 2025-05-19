import sys
sys.setrecursionlimit(100000)
n, m = map(int, sys.stdin.readline().split())
li = []
for _ in range(n):
    s = sys.stdin.readline().strip()
    tmp = []
    for i in s:
        if i == 'H':
            tmp.append(-1)
            continue
        tmp.append(int(i))
    li.append(tmp)

visited = [[False] * m for _ in range(n)]
d = [[0] * m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    if not (0 <= x < n and 0 <= y < m) or li[x][y] == -1:
        return 0
    if visited[x][y]:
        print(-1)
        sys.exit()

    if d[x][y]:
        return d[x][y]

    visited[x][y] = True
    move = li[x][y]
    max_val = 0

    for i in range(4):
        nx = x + dx[i] * move
        ny = y + dy[i] * move
        max_val = max(max_val, dfs(nx, ny) + 1)

    d[x][y] = max_val
    visited[x][y] = False
    return d[x][y]

print(dfs(0, 0))


# ws어려움
# 백트래킹 + dfs + dp
# 특정조건하에 최장 경로 구하기.. 문제 나오면 이 구조일 확률이 있을 듯

# def dfs(x, y):
#     if not (0 <= x < n and 0 <= y < m) or li[x][y] == -1:
#         return 0
#           보드 바깥 or 구멍(H)에 도달한 경우 → 이 경로는 더 이상 못 가니까 0 반환
#           이는 max_val = max(max_val, dfs(...) + 1)의 대상이 되지 않게 만들기 위한 return 0

#     if visited[x][y]:
#         print(-1)
#         sys.exit()
#           현재 경로에서 또 들어오면 → 무한 루프 가능성 → 즉시 종료
#           핵심은 "현재 탐색 중인 경로"에만 적용해야 한다는 것
#           → 그래서 백트래킹으로 다시 False 처리 필요

#     if d[x][y]:
#         return d[x][y]
#           이미 (x, y)에서 최대 이동 수를 계산했으면 → 그 값 재사용
#           시간 절약 + 재귀 깊이 제한 방지

#     visited[x][y] = True
#     move = li[x][y]
#     max_val = 0
#           방문 처리 후, 상하좌우 move칸씩 이동
#           그 중 가장 긴 경로를 선택하여 +1 (현재 이동 포함)
#
#     for i in range(4):
#         nx = x + dx[i] * move
#         ny = y + dy[i] * move
#         max_val = max(max_val, dfs(nx, ny) + 1)
#               현재 위치에서 갈 수 있는 최장 경로 계산
#
#     d[x][y] = max_val
#     visited[x][y] = False
#     return d[x][y]