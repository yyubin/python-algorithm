import sys
from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    q = deque([1])
    visited = [0] * (n+1)

    while q:
        now = q.popleft()
        for next in graph[now]:
            if visited[next] == 0 and next != 1:
                visited[next] = visited[now] + 1
                q.append(next)


    max_ = max(visited)
    return visited.count(max_)

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
