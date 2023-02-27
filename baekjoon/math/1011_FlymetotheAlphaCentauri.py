import sys
t = int(sys.stdin.readline())

for _ in range(t):
    x, y = map(int, sys.stdin.readline().rstrip().split())

    d = y - x

    ans = 1
    while True:
        if d <= ans*(ans+1):
            break
        ans += 1

    if d <= ans**2:
        print(ans*2 - 1)
    else:
        print(ans*2)

# 처음 이동 거리, 마지막 이동 거리는 무조건 1
# 거리가 8일 경우 1, 2, 2, 2, 1

# 1: 1
# 2: 1 1
# 3: 1 1 1
# 4: 1 2 1
# 5: 1 2 1 1
# 6: 1 2 2 1
# 7: 1 2 2 1 1
# 8: 1 2 2 2 1
# 9: 1 2 3 2 1
# 10: 1 2 3 2 1 1
# 11: 1 2 3 2 2 1
# ...

# y - x = 1
# y - x = 1 + 1
# y - x = 1 + 1 + 1
# y - x = 1 + 1 + 2
# y - x = 1 + 1 + 2 + 2
# y - x = 1 + 1 + 2 + 2 + 3

# 작동 횟수
# 반복 횟수가 같은 것들 끼리 더하면
# 2*1, 2*2, 2*3, ... , 2*n
# 총 이동 거리가 n의 제곱보다 작거나 같으면 n*2-1
# n의 제곱보다 크면 n*2

