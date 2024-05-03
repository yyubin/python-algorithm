from itertools import combinations

for tc in range(1, int(input())+1):
    n, k = map(int, input().split())
    li = list(map(int, input().split()))

    cnt = 0
    for i in range(1, n+1):
        for comb in combinations(li, i):
            if sum(comb) == k:
                cnt += 1

    print(f'#{tc} {cnt}')

