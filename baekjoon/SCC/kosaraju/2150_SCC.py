import sys
sys.setrecursionlimit(10 ** 6)

v, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(v+1)]
reverse_graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    reverse_graph[b].append(a)

visited = [False] * (v+1)
stack = []

def dfs1(v):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs1(u)
    stack.append(v)

for v in range(1, v+1):
    if not visited[v]:
        dfs1(v)

visited = [False] * (v+1)
scc_result = []

def dfs2(v, scc):
    visited[v] = True
    scc.append(v)

    for u in reverse_graph[v]:
        if not visited[u]:
            dfs2(u, scc)

while stack:
    v = stack.pop()
    if not visited[v]:
        scc = []
        dfs2(v, scc)
        scc_result.append(sorted(scc))

scc_result.sort(key=lambda x: x[0])
print(len(scc_result))
for comp in scc_result:
    print(' '.join(map(str, comp)), end=" -1\n")