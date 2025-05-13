import sys

n, k = map(int, sys.stdin.readline().split())
li = [int(sys.stdin.readline()) for _ in range(n)]
visited = [False] * n
cur = 0
cnt = 0

while not visited[cur]:
    visited[cur] = True
    cnt += 1
    cur = li[cur]
    if cur == k:
        print(cnt)
        break
else:
    print(-1)


# def dfs(start, x, tmp_visited):
#     tmp_visited[x] = True
#     if x == k:
#         return start
#     if not tmp_visited[li[x]]:
#         return dfs(start, li[x], tmp_visited)
#     return sys.maxsize
#
# res = sys.maxsize
# for i in range(1, n + 1):
#     visited = [False] * (n + 1)
#     result = dfs(i, i, visited)
#     print(result)
#     res = min(res, result)
# print(-1 if res == sys.maxsize else res)

# 문제에서 0이 최초로 시작할때 1번을 부르는 거라고 제시되어있는걸 놓침