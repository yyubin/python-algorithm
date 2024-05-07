from collections import deque

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9


def bfs(start):
    q = deque([start])
    visited[start] = True

    while q:
        value = q.popleft()
        print(value, end=" ")

        for i in graph[value]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


bfs(1)
