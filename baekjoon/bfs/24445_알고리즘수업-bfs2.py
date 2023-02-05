from collections import deque
import sys

n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort(reverse=True)


def bfs(r):
    cnt = 1
    queue = deque([r])
    visited[r] = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                cnt += 1
                visited[i] = cnt


bfs(r)

print(*visited[1:], sep="\n")


# 왜 visited로 결과구현하면 맞는데 result따로 만들면 안되지..?
