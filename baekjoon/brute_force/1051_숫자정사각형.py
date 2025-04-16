import sys
n, m = map(int, sys.stdin.readline().split())
li = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
res = 1
for i in range(n):
    for j in range(m):
        now = li[i][j]
        for k in range(1, min(n-i, m-j)):
            if li[i][j] == li[i][j+k] == li[i+k][j] == li[i+k][j+k]:
                res = max(res, (k+1)**2)
print(res)

## 그냥 하나씩 늘려가면서 검사하는게 나음
#         for k in range(i+1, n):
#             if li[k][j] == now and j+k < m and li[i][k+j] == now and li[k][j+k] == now:
#                 res = max(res, (k+1)**2)
# 이렇게하면 k가 행간 거리를 의미하므로 정확히 j를 표현할수없음..