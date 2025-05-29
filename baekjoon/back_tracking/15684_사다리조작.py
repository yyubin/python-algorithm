import sys
n, m, h = map(int, sys.stdin.readline().split())
ladder = [[0] * (n+1) for _ in range(h+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    ladder[a][b] = 1
    ladder[a][b+1] = -1

def check(x):
    for k in range(1, n+1):
        j = k
        for i in range(1, h+1):
            j += x[i][j]
        if j != k:
            return False
    return True

ans = sys.maxsize
def dfs(cnt, idx):
    global ans
    if check(ladder):
        ans = min(ans, cnt)
        return
    elif cnt == 3 or ans <= 3:
        return

    for i in range(idx, len(graph)):
        if not ladder[graph[i][0]][graph[i][1]] and not ladder[graph[i][0]][graph[i][1]+1]:
            ladder[graph[i][0]][graph[i][1]] = 1
            ladder[graph[i][0]][graph[i][1]+1] = -1
            dfs(cnt+1, i+1)
            ladder[graph[i][0]][graph[i][1]] = 0
            ladder[graph[i][0]][graph[i][1]+1] = 0

graph = []
for i in range(1, h+1):
    for j in range(1, n):
        if not ladder[i][j] and not ladder[i][j+1]:
            graph.append((i, j))
dfs(0, 0)
print(ans if ans < 4 else -1)
