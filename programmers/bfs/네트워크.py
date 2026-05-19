from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(x, visited, graph):
    q = deque()
    q.append(x)
    visited[x] = True

    while q:
        now = q.popleft()
        for k in graph[now]:
            if not visited[k]:
                visited[k] = True
                q.append(k)


def solution(n, computers):
    visited = [False] * (n + 1)
    cnt = 0
    graph = [[] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1:
                graph[i].append(j)

    for i in range(n):
        if not visited[i]:
            bfs(i, visited, graph)
            cnt += 1

    return cnt

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))