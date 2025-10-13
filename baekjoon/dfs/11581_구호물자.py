import sys
sys.setrecursionlimit(10 ** 6)
n = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    _ = int(sys.stdin.readline())
    graph[i+1].extend(list(map(int, sys.stdin.readline().split())))

def dfs(start):
    if start == n:
        return
    visited[start] = 1

    for v in graph[start]:
        if visited[v] == 0:
            dfs(v)
        elif visited[v] == 1:
            print('CYCLE')
            sys.exit()

    visited[start] = 2

visited = [0] * (n + 1)
dfs(1)
print('NO CYCLE')