import sys
sys.setrecursionlimit(10**6)
t = int(sys.stdin.readline())


def dfs(now):
    global cnt
    visited[now] = True
    next = li[now]

    if not visited[next]:
        dfs(next)
    else:
        if next not in team:
            tmp = next
            while tmp != now:
                cnt += 1
                tmp = li[tmp]
            cnt += 1

    team.add(now)


for _ in range(t):
    n = int(sys.stdin.readline())
    li = [0] + list(map(int, sys.stdin.readline().split()))

    visited = [False] * (n + 1)
    team = set()
    cnt = 0

    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)

    print(n - cnt)

