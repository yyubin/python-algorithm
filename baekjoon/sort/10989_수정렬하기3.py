import sys
n = int(sys.stdin.readline())
d = [0] * 10001

for _ in range(n):
    a = int(sys.stdin.readline())
    d[a] += 1

for i in range(10001):
    if d[i] != 0:
        for j in range(d[i]):
            print(i)

## 메모리 제한 문제