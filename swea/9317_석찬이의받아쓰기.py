for tc in range(1, int(input())+1):
    n = int(input())
    a = list(map(str, input()))
    b = list(map(str, input()))
    res = 0
    for i in range(n):
        if a[i] == b[i]:
            res += 1

    print(f'#{tc} {res}')
