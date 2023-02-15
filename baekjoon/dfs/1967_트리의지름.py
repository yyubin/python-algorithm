import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
graph = [[] for i in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dfs(start, cost):
    for i in graph[start]:
        if distance[i[0]] == -1:
            distance[i[0]] = cost + i[1]
            dfs(i[0], distance[i[0]])


distance = [-1 for i in range(n+1)]
distance[1] = 0
dfs(1, 0)
start = distance.index(max(distance))

distance = [-1 for i in range(n+1)]
distance[start] = 0
dfs(start, 0)

print(max(distance))

# 트리의 지름 증명
# 1. 트리에서 아무 노드나 잡고 그 노드에 대한 가장 먼 노드를 구하고 이 노드를 n1이라고 하자.
# 2. n1 에대한 가장 먼 노드를 한번 더 구한다. 이 노드를 n2라고 하자.
# 3. 이제 n1과 n2의 거리가 트리의 지름이 된다.
# 귀류법 증명 블로그 : https://koosaga.com/14


