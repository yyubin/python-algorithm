import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
visited = [-1] * 100001

cnt = 0
def bfs(x):
    global cnt
    q = deque()
    q.append(x)
    visited[x] = 0
    while q:
        a = q.popleft()
        for i in [a*2]:
            if 0 <= i < 100001:
                if visited[i] == -1 or visited[i] > visited[a]:
                    visited[i] = visited[a]
                    q.append(i)

        for i in [a+1, a-1]:
            if 0 <= i < 100001:
                if visited[i] == -1 or visited[i] >= visited[a] + 1:
                    visited[i] = visited[a] + 1
                    q.append(i)


bfs(n)
print(visited[k])

