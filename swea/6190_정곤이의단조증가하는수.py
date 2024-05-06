from itertools import combinations
for tc in range(1, int(input())+1):
    n = int(input())
    li = list(map(int, input().split()))
    tmp = [-1]

    for cb in combinations(li, 2):
        tmp_num = cb[0] * cb[1]
        if max(tmp) > tmp_num:
            continue

        tmp_li = list(map(int, str(tmp_num)))
        now = tmp_li[0]
        for i in tmp_li:
            if now > i:
                break
            now = i
        else:
            tmp.append(tmp_num)

    print(f'#{tc} {max(tmp)}')
