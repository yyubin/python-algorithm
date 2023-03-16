import math
import sys
n = int(sys.stdin.readline())

prime_number = []
li = [True for _ in range(n+1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if li[i]:
        j = 2

        while i * j <= n:
            li[i*j] = False
            j += 1

for num in range(2, n+1):
    if li[num]:
        prime_number.append(num)

# n까지의 소수 모두 구해두기

cnt = 0
right_sum = 0
end = 0

for start in range(len(prime_number)):
    # 구해둔 소수 배열 돌면서
    # right_sum은 n보다 작고 end는 소수 배열 크기보다 작을때까지
    while right_sum < n and end < len(prime_number):
        # 배열에 prime_number[end]를 더해줌
        # 그럼 prime_number의 0부터 더해짐
        # 2, 3, 5, 7, ...
        right_sum += prime_number[end]
        end += 1

    # right_sum이 n보다 더 큰 경우는 제외하고
    # n이 같을 경우 cnt 증가
    if right_sum == n:
        cnt += 1
    # right_sum에 이제 prime_num[start]를 빼줌
    # 2, 3, 5, 7, 11이 더해진 경우
    # 2를 제거함 아제 나머지의 합이 n보다 작을 경우 다시 while문 돌면서 더해주고
    # 아닐 경우 다시 n과 비교
    right_sum -= prime_number[start]

print(cnt)