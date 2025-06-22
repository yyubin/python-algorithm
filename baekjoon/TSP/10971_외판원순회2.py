import sys
def tsp(cost):
    from functools import lru_cache

    n = len(cost)

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
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(tsp(cost))
