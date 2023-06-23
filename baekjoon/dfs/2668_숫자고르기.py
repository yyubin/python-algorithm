import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(n)]


def dfs(x, goal):
    if li[x-1] == goal:
        return True

    if not visited[x]:
        visited[x] = True
        if dfs(li[x-1], goal):
            return True

    else:
        return False


result = []
for i, v in enumerate(li):
    if i+1 == v:
        result.append(v)
        continue

    visited = [False] * (n+1)
    if dfs(i+1, i+1):
        result.append(v)

result.sort()
print(len(result))
print(*result, sep="\n")
