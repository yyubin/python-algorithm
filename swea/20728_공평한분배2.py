for tc in range(int(input())):
    n, k = map(int, input().split())
    li = list(map(int, input().split()))

    li.sort(reverse=True)

    res = 10e9
    for i in range(n-k+1):
        if li[i] - li[i+(k-1)] < res:
            res = li[i] - li[i+(k-1)]

    print(f'#{tc+1} {res}')