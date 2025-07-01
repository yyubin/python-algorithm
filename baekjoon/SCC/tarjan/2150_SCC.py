import sys
sys.setrecursionlimit(10 ** 6)
v, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

ids = [0] * (v+1)
low = [0] * (v+1)
on_stack = [False] * (v+1)
stack = []
scc_result = []
id_count = 1

def dfs(v):
    global id_count
    ids[v] = low[v] = id_count
    id_count += 1
    stack.append(v)
    on_stack[v] = True

    for u in graph[v]:
        if ids[u] == 0:
            dfs(u)
            low[v] = min(low[v], low[u])
        elif on_stack[u]:
            low[v] = min(low[v], ids[u])

    if ids[v] == low[v]:
        scc = []
        while True:
            u = stack.pop()
            on_stack[u] = False
            scc.append(u)
            if u == v:
                break
        scc_result.append(sorted(scc))

for v in range(1, v+1):
    if ids[v] == 0:
        dfs(v)

scc_result.sort(key=lambda x: x[0])
print(len(scc_result))
for comp in scc_result:
    print(' '.join(map(str, comp)), end=" -1\n")