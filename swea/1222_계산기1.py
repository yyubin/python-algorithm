for tc in range(1, 11):
    n = int(input())
    li = list(map(int, input().split('+')))
    print(f'#{tc} {sum(li)}')
