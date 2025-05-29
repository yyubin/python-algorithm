import sys
from collections import deque
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    li = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    graph = [[False] * (n+1) for _ in range(n+1)]
    degree = [0 for _ in range(n+1)]

    for i in range(n):
        for j in range(i+1, n):
            higher = li[i]
            lower = li[j]
            graph[higher][lower] = True
            degree[lower] += 1

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            degree[b] -= 1
            degree[a] += 1
        else:
            graph[b][a] = False
            graph[a][b] = True
            degree[a] -= 1
            degree[b] += 1

    q = deque()
    for i in range(1, n+1):
        if degree[i] == 0:
            q.append(i)

    result = []
    is_certain = True
    is_cycle = False

    for _ in range(n):
        if not q:
            is_cycle = True
            break
        if len(q) > 1:
            is_certain = False

        now = q.popleft()
        result.append(now)

        for j in range(1, n+1):
            if graph[now][j]:
                degree[j] -= 1
                if degree[j] == 0:
                    q.append(j)

    if is_cycle:
        print("IMPOSSIBLE")
    elif not is_certain:
        print("?")
    else:
        print(*result, sep=' ')

# 작년 순위 기으로 올해 순위 그래프를 만들어서
# 주어진 정보에 따라 그래프를 역전 시킴
# 이걸 위상정렬로 정렬 가능한지 확인함

# 위상정렬 결과가 1개인 경우 -> 정상 출력
# 위상정렬 중 원소가 2개 이상 존재하면 -> 불분명
# 위상정렬 불가능한 경우 -> 사이클