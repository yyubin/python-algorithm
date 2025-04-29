import sys
n, m = map(int, sys.stdin.readline().split())
p = [int(sys.stdin.readline().rstrip()) for _ in range(m)]
p.sort(reverse=True)
res = 0
price = 0
for i in p:
    cnt = 0
    for j in p:
        if j >= i:
            cnt += 1
    cnt = min(cnt, n)
    if res < cnt * i:
        res = cnt * i
        price = i

print(price, res)