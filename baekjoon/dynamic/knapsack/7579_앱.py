import sys
n, m = map(int, sys.stdin.readline().split())
memory = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

max_cost = sum(cost)
dp = [0] * (max_cost + 1)

for i in range(n):
    now_c = cost[i]
    now_m = memory[i]

    for j in range(max_cost, now_c-1, -1):
        dp[j] = max(dp[j], dp[j-now_c] + now_m)

for i in range(max_cost+1):
    if dp[i] >= m:
        print(i)
        break

# 풀이 -> 배낭문제
# 메모리가 최대 천만이라 cost를 기준으로 dp 테이블 만들고
# 최대 비용에서 현재 가능한 비용까지 거꾸로 순회하면서
# 가방에 넣을 수 있는 경우만 탐색
# 만약 지금 가방에 넣는게 더 큰 값이면 할당

# 최대 비용까지 순회하면서 m보다 큰 값이 있으면 해당 코스트 출력

# 쉽지않은데
# 나중에 다시 풀어봐야할듯

# 시간 복잡도 O(sum(cost) * n) + O(sum(cost))
# cost, n 모두 최대 100
# sum(cost) ≈ 10000 (최대 100개의 앱 × 최대 비용 100)
# O(N×∑cost)

