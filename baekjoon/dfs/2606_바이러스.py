# 2606번 바이러스 (dfs)
computer = int(input())
num = int(input())
visited = [False] * (computer + 1)
graph = [[]]

for _ in range(num):
    d = list(map(int, input().split()))
    graph.append(d)
    graph.append(d[::-1])


def dfs(v: int):
    visited[v] = True

    for i in range(1, len(graph)):
        if graph[i][0] == v and not visited[graph[i][1]]:
            dfs(graph[i][1])
    return


dfs(1)
print(visited.count(True) - 1)
