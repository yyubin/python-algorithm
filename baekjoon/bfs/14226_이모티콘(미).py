import sys
from collections import deque
n = int(sys.stdin.readline())
visited = [False] * (n*3)

q = deque()
q.append((1, 0, 0))

while q:
    now, bff, cnt = q.popleft()
    print(now, bff, cnt)
    if now == n:
        print(cnt)
        break




    for i in range(3):
        if i == 0 and not visited[now]:
            visited[now] = True
            bff = now
            q.append((now, bff, cnt+1))
        elif i == 1 and bff and now+bff > 0 and not visited[now+bff]:
            visited[now+bff] = True
            q.append((now+bff, bff, cnt+1))
        elif i == 2 and now-1 >= 0 and not visited[now-1]:
            visited[now-1] = True
            q.append((now-1, bff, cnt+1))
