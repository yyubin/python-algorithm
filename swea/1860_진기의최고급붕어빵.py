for tc in range(1, int(input())+1):
    n, m, k = map(int, input().split())
    people = list(map(int, input().split()))

    result = 'Possible'

    people.sort()

    for i, v in enumerate(people):
        if (v//m)*k - i <= 0:
            result = 'Impossible'
            break

    print(f'#{tc} {result}')



