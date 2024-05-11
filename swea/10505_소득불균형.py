for tc in range(1, int(input())+1):
    n = int(input())
    li = list(map(int, input().split()))
    avg = sum(li)//n
    res = 0
    for i in li:
        if avg >= i:
            res +=1

    print(f'#{tc} {res}')
