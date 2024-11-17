import sys
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ans = []

    for i in range(2, n+1):
        cnt = 0
        while n%i == 0:
            cnt += 1
            n //= i
        if cnt:
            ans.append([i, cnt])

    for i in ans:
        print(*i)


# 굳이 소수판별할 이유없음
