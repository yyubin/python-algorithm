import sys
for _ in range(int(sys.stdin.readline())):
    n, m, k = map(int, sys.stdin.readline().split())
    homes = list(map(int, sys.stdin.readline().split()))
    homes += homes
    now = sum(homes[:m])
    res = 1 if now < k else 0

    if n == m:
        print(res)
        continue

    for i in range(n-1):
        now -= homes[i]
        now += homes[i+m]
        if now < k:
            res += 1

    print(res)
