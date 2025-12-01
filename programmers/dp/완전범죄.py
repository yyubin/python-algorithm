# 2025 프로그래머스 코드챌린지 2차 예선

def solution(info, n, m):
    N = len(info)
    dp = [[[False] * (m + 1) for _ in range(n + 1)] for _ in range(N + 1)]
    dp[0][0][0] = True

    for i in range(N):
        aa, bb = info[i]
        for a in range(n+1):
            for b in range(m+1):
                if not dp[i][a][b]:
                    continue
                if a + aa < n:
                    dp[i+1][a+aa][b] = True
                if b + bb < m:
                    dp[i+1][a][b+bb] = True

    ans = int(1e9)
    for i in range(n):
        for j in range(m):
            if dp[N][i][j]:
                ans = min(ans, i)

    return ans if ans != 1e9 else -1

print(solution([[1, 2], [2, 3], [2, 1]], 4, 4))
print(solution([[1, 2], [2, 3], [2, 1]], 1, 7))
print(solution([[3, 3], [3, 3]], 7, 1))
print(solution([[3, 3], [3, 3]], 6, 1))
