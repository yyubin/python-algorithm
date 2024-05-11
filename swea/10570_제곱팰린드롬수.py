for tc in range(1, int(input())+1):
    a, b = map(int, input().split())
    li = [i for i in range(a, b+1)]
    palin = [1, 4, 9, 121, 484]
    res = 0
    for i in palin:
        res += li.count(i)
    print(f'#{tc} {res}')
