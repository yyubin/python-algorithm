INF = 10**15
def dfs(graph, dp, u):
    dp[u][0] = 0
    dp[u][1] = graph[u][0]

    extra = INF
    has_attendee = False

    for v in graph[u][1]:
        dfs(graph, dp, v)

        dp[u][1] += min(dp[v][0], dp[v][1])

        if dp[v][1] <= dp[v][0]:
            dp[u][0] += dp[v][1]
            has_attendee = True
        else:
            dp[u][0] += dp[v][0]
            extra = min(extra, dp[v][1] - dp[v][0])

    if graph[u][1] and not has_attendee:
        dp[u][0] += extra

def solution(sales, links):
    graph = {i + 1: [sales[i], []] for i in range(len(sales))}

    for s, e in links:
        graph[s][1].append(e)

    dp = [[0, 0] for _ in range(len(sales) + 1)]
    dfs(graph, dp, 1)

    return min(dp[1][0], dp[1][1])

print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))
print(solution([5, 6, 5, 3, 4], [[2,3], [1,4], [2,5], [1,2]]))
print(solution([5, 6, 5, 1, 4],  	[[2,3], [1,4], [2,5], [1,2]]))