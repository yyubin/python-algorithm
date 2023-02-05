# 11724 연결 요소의 개수
n, m = map(int, input().split())
graph = [[]]
visited = [False] * (n + 1)

for _ in range(m):
    d = list(map(int, input().split()))
    graph.append(d)
    graph.append(d[::-1])

def dfs(v: int):
    visited[v] = True

    for i in range(1, len(graph)):
        if graph[i][0] == v and not visited[graph[i][1]]:
            dfs(graph[i][1])
    return True


cnt = 0
for i in range(1, len(graph)):
    if not visited[graph[i][0]]:
        if dfs(graph[i][0]):
            cnt += 1

print(cnt + (visited.count(False) - 1))