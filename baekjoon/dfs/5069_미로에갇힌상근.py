import sys
sys.setrecursionlimit(10 ** 6)
dx, dy = [1, -1, 0, 0, 1, -1], [0, 0, 1, -1, -1, 1]
def dfs(x, y, depth):
    if depth == n:
        return 1 if (x, y) == (0, 0) else 0
    key = (x, y, depth)
    if key in memo:
        return memo[key]
    total = 0
    for i in range(6):
        ddx = dx[i] + x
        ddy = dy[i] + y
        total += dfs(ddx, ddy, depth + 1)

    memo[key] = total
    return total

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    memo = {}
    print(dfs(0, 0, 0))

# dp문제인데 dfs+메모이제이션
# 최대 n 14라 시간복잡도 가능
# 매 단계 6방향으로 이동하므로 O(6^n)
# 다만 중복 호출 피하기 때문에 ㄱㄱㅊ
# 메모이제이션으로 저장하는 상태 -> depth n+1 개(0까지), x, y는 각각 n, O(n^3)
# 음수가능하기 때문에 visited는 key(x, y, depth)로 관리


### 그래프에서 n번 이동해서 시작점으로 돌아오는 경로의 수 → DFS + 가지치기