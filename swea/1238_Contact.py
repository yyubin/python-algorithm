from collections import deque

def bfs(x):
    q = deque([[x, 1]])
    visited[x][0] = True

    while q:
        now, count = q.popleft()
        for i in graph[now]:
            if not visited[i][0]:
                visited[i][0] = True
                visited[i][1] = count + 1
                q.append([i, count + 1])



for k in range(10):
    le, start = map(int, input().split())
    li = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    visited = [[False, 0] for i in range(101)]

    for i in range(0, len(li), 2):
        graph[li[i]].append(li[i+1])

    bfs(start)

    max_ = 0
    res_ = 0

    for i in range(1, 101):
        if max_ <= visited[i][1]:
            max_ = visited[i][1]
            res_ = i

    print('#'+str(k+1), res_)



# bfs에서 들어간 순서 확인시, visited에 추가 컬럼만들어서 메모하면서 가기
