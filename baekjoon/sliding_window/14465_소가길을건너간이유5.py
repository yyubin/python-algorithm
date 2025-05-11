import sys
n, k, b = map(int, sys.stdin.readline().split())
li = [1] * (n+1)
for _ in range(b):
    a = int(sys.stdin.readline())
    li[a] = 0

tmp = sum(li[1:k+1])
res = 0
for i in range(2, n+2-k):
    tmp -= li[i-1]
    tmp += li[i+k-1]
    res = max(tmp, res)

print(k - res if k > res else 0)

# 정해진 구간을 살펴보는 문제는 슬라이딩 윈도우일지 생각해봐야함
# 정해진 구간 제시시, 생각해 볼 것
