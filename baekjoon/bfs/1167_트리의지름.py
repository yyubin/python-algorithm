import sys
from collections import deque
v = int(sys.stdin.readline())
graph = [[] for _ in range(v+1)]

for _ in range(v):
    tmp = list(map(int, sys.stdin.readline().split()))
    node = tmp[0]
    idx = 1
    while tmp[idx] != -1:
        tmp_node, tmp_cost = tmp[idx], tmp[idx+1]
        graph[node].append((tmp_node, tmp_cost))
        idx += 2

def bfs(idx):
    q = deque()
    q.append((idx, 0))
    visited = [False for _ in range(v + 1)]
    visited[idx] = True
    result = [0, 0]

    while q:
        now_node, now_cost = q.popleft()
        for nxt_node, nxt_cost in graph[now_node]:
            if not visited[nxt_node]:
                visited[nxt_node] = True
                n_cost = now_cost + nxt_cost
                q.append((nxt_node, n_cost))
                if result[1] < n_cost:
                    result[1] = n_cost
                    result[0] = nxt_node
    return result

res_node, res_cost = bfs(1)
print(bfs(res_node)[1])




