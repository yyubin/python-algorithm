# 분할정복을 통한 거듭제곱
import sys

a, b, c = map(int, sys.stdin.readline().split())


def power(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a % c
    tmp = power(a, n // 2)
    if n % 2 == 0:
        return (tmp * tmp) % c
    else:
        return (tmp * tmp * a) % c


print(power(a, b))



# 지수 법칙 :A^m+n = A^m x A^n
# 나머지 분배 법칙 : (AxB)%C = (A%C) *(B%C) % C

# 10^11 % 12
# = ((10^5)%12 x (10^5)%12 x 10)% 12
# = ((10^2)%12 x (10^2)%12 x 10) %12 x (10^2)%12 x (10^2)%12 x 10) %12 x 10) %12