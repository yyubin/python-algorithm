for tc in range(1, 11):
    n = int(input())
    table = [list(map(str, input().split())) for _ in range(100)]
    table = list(zip(*table))

    result = 0
    for i in table:
        result += ''.join(i).replace('0', '').count('12')

    print(f'#{tc} {result}')
