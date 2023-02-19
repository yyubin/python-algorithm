import sys
tc = int(sys.stdin.readline())

def bfs(V):
    queue = [V]
    visited[V] = 1
    while queue:
        V = queue[0]
        queue.pop(0)
        next = graph[V] #graph[V]의 값
        if visited[next] == 0: #visited[graph[V]] 에 방문하지 않으면
            visited[next] = 1 # 방문처리 후 큐에 넣기
            queue.append(next)
    return 1 # 모든 방문이 끝나면(visited가 전부 1) 한사이클 완료, 리턴

for _ in range(tc):
    n = int(sys.stdin.readline())
    graph = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [0] * (n+1)
    result = 0

    for i in range(1, n+1):
        if visited[i] == 0:
            result += bfs(i)
    print(result)


