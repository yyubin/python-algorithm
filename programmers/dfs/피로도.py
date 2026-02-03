
def solution(k, dungeons):
    res = 0

    def dfs(now, cnt, visited):
        nonlocal res
        res = max(res, cnt)

        for i, v in enumerate(dungeons):
            if not visited[i] and v[0] <= now:
                visited[i] = True
                dfs(now - v[1], cnt+1, visited)
                visited[i] = False

    n = len(dungeons)
    visited = [False] * n
    dfs(k, 0, visited)
    return res

print(solution(80, [[80,20],[50,40],[30,10]]))