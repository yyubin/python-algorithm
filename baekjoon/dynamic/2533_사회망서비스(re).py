import sys
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

#d[i][1] 자신이 얼리어답터인 경우, 자식이 얼리어답터이든 아니든 작은 값 넣어주기
#d[i][0] 자신이 얼리어답터가 아닌 경우, 자식 노드가 무조건 얼리어답터여야 함, += d[j][1]
d = [[0, 0] for _ in range(n+1)]
visited = [False] * (n+1)

def dfs(x):
    visited[x] = True
    d[x][0] = 0
    d[x][1] = 1
    for i in graph[x]:
        if not visited[i]:
            dfs(i)
            d[x][0] += d[i][1]
            d[x][1] += min(d[i][0], d[i][1])

dfs(1)
print(min(d[1][0], d[1][1]))

