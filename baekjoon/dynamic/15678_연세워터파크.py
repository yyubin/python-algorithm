import sys
from collections import deque
n, d = map(int, sys.stdin.readline().split())
dp = [0] + list(map(int, sys.stdin.readline().split()))

q = deque()
for i in range(1, n+1):
    while q:
        if q[0][0] < i-d:
            q.popleft()
        else:
            dp[i] = max(dp[i], dp[i] + q[0][1])
            break

    while q:
        if q[-1][1] < dp[i]:
            q.pop()
        else:
            break

    q.append((i, dp[i]))

print(max(dp[1:]))

# 단조 큐 사용
# 구간 조건에 안맞는것들 앞에서 빼기
# 큐에 넣기전에 큰값들 모두 제거 -> 현재 넣으려는 수보다 큰 수 무시

# q[0]는 범위 내 dp값 중 가장 큰 값을 가지고 있음, 이걸 써서 dp[i] 갱신하는 것

# 들어올 값보다 작으면 모두 제거하는건
# 단조 큐 유지 -> 나보다 작은 값은 쓰일 일이 없어서