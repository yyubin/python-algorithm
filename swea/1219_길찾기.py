from collections import deque

for tc in range(1, 11):
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    graph = [[] for _ in range(100)]
    visited = [0] * 100

    que = deque(li)
    while len(que) > 0:
        a = que.popleft()
        b = que.popleft()
        graph[a].append(b)

    q = deque([0])
    visited[0] = 1

    while q:
        now = q.popleft()
        if now == 99:
            visited[99] = 1
            break
        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)

    print(f'#{tc} {visited[99]}')
