import sys
sys.setrecursionlimit(10 ** 6)
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

d = [[0, 0] for _ in range(n+1)]
visited = [False] * (n+1)
path = [[[] for _ in range(2)] for _ in range(n+1)]

def dfs(x):
    visited[x] = True
    d[x][1] = li[x-1]
    path[x][1] = [x]

    for i in graph[x]:
        if not visited[i]:
            dfs(i)
            if d[i][1] >= d[i][0]:
                d[x][0] += d[i][1]
                path[x][0] += path[i][1]
            else:
                d[x][0] += d[i][0]
                path[x][0] += path[i][0]
            d[x][1] += d[i][0]
            path[x][1] += path[i][0]

dfs(1)

if d[1][0] > d[1][1]:
    print(d[1][0])
    path[1][0].sort()
    print(*path[1][0])
else:
    print(d[1][1])
    path[1][1].sort()
    print(*path[1][1])

# dp 배열은 각 노드에서 최대 가중치의 합을 저장
# dp[i][0]은 i번 노드를 포함하지 않을 때의 최대 합, dp[i][1]은 i번 노드를 포함할 때의 최대 합을 의미
# dp[s][1]과 path[s][1]은 항상 s번 노드를 포함하는 배열이기 때문에 자식노드들이 포함되지 않는 [i][0]의 값들을 더함