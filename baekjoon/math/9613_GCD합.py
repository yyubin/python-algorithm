import sys
import math

cnt = int(sys.stdin.readline())

for _ in range(cnt):
    li = list(map(int, sys.stdin.readline().rstrip().split()))
    result = []

    for i in range(1, len(li)):
        for j in range(i + 1, len(li)):
            result.append(math.gcd(li[i], li[j]))

    print(sum(result))
