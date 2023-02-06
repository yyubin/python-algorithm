import sys
import math


def is_prime(num: int):
    for k in range(2, int(math.sqrt(num)) + 1):
        if num % k == 0:
            return False
    return True


while True:
    num = int(sys.stdin.readline())
    if num == 0:
        break

    cnt = 0
    for i in range(num + 1, 2 * num + 1):
        if is_prime(i) and i != 1:
            cnt += 1

    print(cnt)
