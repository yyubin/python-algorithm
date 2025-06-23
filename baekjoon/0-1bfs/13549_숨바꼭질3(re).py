import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
visited = dict()

q = deque([n])
visited[n] = 0

while q:
    now = q.popleft()
    if now == k:
        print(visited[now])
        break

    for i in [2 * now, now - 1, now + 1]:
        if 0 <= i <= 200000 and i not in visited:
            if i == 2 * now:
                visited[i] = visited[now]
                q.appendleft(i)
            else:
                visited[i] = visited[now] + 1
                q.append(i)

