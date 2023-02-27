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
        if a == k:
            cnt += 1
        for i in [a*2, a+1, a-1]:
            if 0 <= i < 100001:
                if visited[i] == -1 or visited[i] >= visited[a] + 1:
                    visited[i] = visited[a] + 1
                    q.append(i)

bfs(n)
print(visited[k])
print(cnt)

