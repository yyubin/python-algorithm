import sys

cnt = 0
while True:
    l, p, v = map(int, sys.stdin.readline().split())
    cnt += 1

    if l == p == v == 0:
        break

    tmp = (v//p)*l
    tmp += min((v%p), l)
    print(f'Case {cnt}: {tmp}')

