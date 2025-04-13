import sys
MOD = 9901
n = int(sys.stdin.readline())
d = [[0] * 3 for _ in range(n+1)]
d[1][0] = 1
d[1][1] = 1
d[1][2] = 1

for i in range(2, n+1):
    d[i][0] = (d[i-1][0] + d[i-1][1] + d[i-1][2]) % MOD
    d[i][1] = (d[i-1][0] + d[i-1][2]) % MOD
    d[i][2] = (d[i-1][0] + d[i-1][1]) % MOD

res = (d[n][0] + d[n][1] + d[n][2]) % MOD
print(res)

# 시간복잡도 O(N)
# 칸별 사자의 가능한 수를 구하려면 인접조건을 무시하게 됨
