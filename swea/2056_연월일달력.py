for tc in range(1, int(input())+1):
    n = list(map(str, input()))
    year, month, day = n[:4], n[4:6], n[6:]

    flag = True
    if 1 > int(''.join(month)) or int(''.join(month)) > 12:
        flag = False

    if flag:
        if int(''.join(month)) in [1, 3, 5, 7, 8, 10, 12]:
            if 1 > int(''.join(day)) or 31 < int(''.join(day)):
                flag = False
        if int(''.join(month)) in [4, 6, 9, 11]:
            if 1 > int(''.join(day)) or 30 < int(''.join(day)):
                flag = False
        if int(''.join(month)) == 2:
            if 1 > int(''.join(day)) or 28 < int(''.join(day)):
                flag = False

    print(f'#{tc} {"".join(year)}/{"".join(month)}/{"".join(day)}' if flag else f'#{tc} -1')
