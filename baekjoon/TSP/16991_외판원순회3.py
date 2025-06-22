import sys
import math
def tsp(cost):
    from functools import lru_cache

    @lru_cache(None)
    def dfs(visited, current):
        if visited == (1 << n) - 1:
            return cost[current][0] if cost[current][0] > 0 else float('inf')
        result = float('inf')
        for next in range(n):
            if not visited & (1 << next) and cost[current][next] > 0:
                result = min(result, dfs(visited | (1 << next), next) + cost[current][next])
        return result

    return dfs(1, 0)

n = int(sys.stdin.readline())
cost = [[0] * n for _ in range(n)]
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            cost[i][j] = float('inf')
            continue
        tmp = math.hypot(graph[i][0] - graph[j][0], graph[i][1] - graph[j][1])
        cost[i][j] = tmp
        cost[j][i] = tmp
print(tsp(cost))

# 실제 유클리드 거리를 원한다면 math.sqrt()를 사용