import sys
n = int(sys.stdin.readline())
d = [0] * 1001
d[1] = 1
d[2] = 2

for i in range(3, 1001):
    d[i] = (d[i-1] + d[i-2])

print(d[n]%10007)

# 솔브닥에서 제출한거 보다가 이거만 고치면 시간 많이 줄듯 싶어서
# 30ms 줄었ㅏ