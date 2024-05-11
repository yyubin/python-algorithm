for tc in range(1, int(input())+1):
    l, u, x = map(int, input().split())
    if x > u:
        result = -1
    elif l <= x <= u:
        result = 0
    else:
        result = l - x
    print(f'#{tc} {result}')
