import sys
n, k = map(int, sys.stdin.readline().split())
ans = 0
while bin(n).count('1') > k:
    idx = bin(n)[::-1].index('1')
    ans += 2 ** idx
    n += 2 ** idx
print(ans)


# 13의 경우
# 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1을 묶어서 2로 2를 묶어서 4로 4를 묶어서 8로 만들면
# 3개의 물병이 남고 8 4 1 리터가 남은상태 여기에서 n개를 더 살수 있음
# 13의 2진수는 1 1 0 1 >> 1이 3개
# 1을 더하면 1 1 1 0 >> 1이 3개
# 2를 더하면 1 0 0 0 0 >> 1개
# 1을 줄이면 됨
# 오른쪽으로 뒤집어서 1을 찾고 그 수의 제곱만큼을 더해주면 됨
