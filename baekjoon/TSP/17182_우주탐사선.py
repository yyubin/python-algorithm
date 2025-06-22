import sys
n, k = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for m in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][m] + graph[m][j]:
                graph[i][j] = graph[i][m] + graph[m][j]

def tsp(cost, start):
    from functools import lru_cache
    n = len(cost)

    @lru_cache(maxsize=None)
    def dfs(visited, current):
        if visited == (1 << n) - 1:
            return 0
        result = sys.maxsize
        for next in range(n):
            if not (visited & (1 << next)):
                result = min(result, dfs(visited | (1 << next), next) + cost[current][next])
        return result
    return dfs(1 << start, start)

print(tsp(graph, k))


# 풀이 방법 : 플로이드 워셜 + tsp

# tsp 와 다른점
# 종료 조건: 더 이상 방문할 곳이 없음 -> 마지막에 다시 최초값 안넣어줘도 됨
# start도 start로 시작해야하고, 해당 visited 표시 위해 1 << start로 기재

# 우선순위큐 + 다익스트라 + bit dp 풀이나
# bfs like + bit dp 풀이도 많은듯??
