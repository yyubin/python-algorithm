import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

end, result = x[0], x[0]

for i in range(1, m):
    tmp = abs(end - x[i])

    if tmp%2 == 0:
        tmp //= 2
    else:
        tmp = (tmp//2) + 1

    result = max(result, tmp)
    end = x[i]

print(max(result, abs(n-x[m-1])))

## 이분탐색으로 전범위 체크하면 시간초과..
