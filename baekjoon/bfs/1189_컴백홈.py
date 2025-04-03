import sys
sys.setrecursionlimit(10 ** 6)
r, c, k = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
res = 0
def dfs(x, y, cnt):
    global res, k
    if x == 0 and y == c-1:
        if cnt == k:
            res += 1
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == '.':
            graph[nx][ny] = 'V'
            dfs(nx, ny, cnt+1)
            graph[nx][ny] = '.'

graph[r-1][0] = 'V'
dfs(r-1, 0, 1)
print(res)

# 방문체크가 유동적으로 되어야 하는 경우 백트래킹+dfs 사용하기
# dfs 시간복잡도 O(n!)
