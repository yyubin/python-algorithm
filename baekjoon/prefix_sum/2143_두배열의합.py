import sys
from collections import defaultdict
t = int(sys.stdin.readline())
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

dic = defaultdict(int)

result = 0

for i in range(n):
    for j in range(i, n):
        dic[sum(a[i:j+1])] += 1
        # 부분합의 결과 각각 카운트
        # key가 부분합,
        # ex) [1] = 1, [2] = 1, [3] = 2 일 경우
        # 부분합이 1인 경우가 한번, 2인 경우가 한번, 3인 경우가 2번

for i in range(m):
    for j in range(i, m):
        result += dic[t - sum(b[i:j+1])]
        # 구하려는 부분합이 5인경우
        # 5 - 3 = 2 인데 dic[2]인 경우를 찾아 누적시켜준다

print(result)


##https://velog.io/@nyanyanyong/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98python%EB%B0%B1%EC%A4%80-2143%EB%91%90-%EB%B0%B0%EC%97%B4%EC%9D%98-%ED%95%A9