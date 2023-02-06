import sys
import math

m = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
result = []


def is_prime(num: int):
    for k in range(2, int(math.sqrt(num))+1):
        if num % k == 0:
            return False
    return True


for i in range(m, n+1):
    if is_prime(i) and i != 1:
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))
