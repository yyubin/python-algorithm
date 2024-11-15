import sys
n = int(sys.stdin.readline())
ans = 0

for i in range(1, n+1):
    ans += (n//i) * i

print(ans)

# 특정 수의 배수는 약수로 특정 수를 포함함
# 3의 배수인 3, 6, 9 는 약수로 3을 포함함
# n 이하의 모든 약수의 합이니
# n 이하를 돌면서 n이 9라면 9//1 9//2 9//3 등
# 1을 약수로 갖는 수의 개수
# 2를 약수로 갖는 수의 개수
# 3을 약수로 갖는 수의 개수를 구한후 해당수로 곱해줌

# 시간초과
# import math
# import sys
# n = int(sys.stdin.readline())
#
# d = [0] * (n+1)
# d[1] = 1
#
# for i in range(2, n+1):
#     tmp = i
#     for j in range(1, i):
#         if i%j == 0:
#             tmp += j
#     d[i] = tmp
#
# print(sum(d))



