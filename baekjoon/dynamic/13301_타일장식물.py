import sys
num = int(sys.stdin.readline().rstrip())
d = [0] * 100

def fibo(num):
    if num <= 2:
        return 1
    if d[num] != 0:
        return d[num]
    d[num] = fibo(num-2) + fibo(num-1)
    return d[num]


if num == 1:
    print(4)
else:
    n = fibo(num)
    print(n*4 + (fibo(num-1))*2)



# 1 -> 4
# 2 -> 6 2만큼 증가
# 3 -> 10  4만큼 증가
# 4 -> 16  6만큼 증가
# 5 -> 26  10만큼 증가
# 6 -> 42  16만큼 증가

# 1, 1, 2, 3, 5, 8, 13 ...

# 1 -> 1 x 4
# 2 -> 1 x 4 + 2(이전 단계의 두배, 1x2)
# 3 -> 2 x 4 + 2(1x2)
# 4 -> 3 x 4 + 4(2x2)
# 5 -> 5 x 4 + 6(3x2)
