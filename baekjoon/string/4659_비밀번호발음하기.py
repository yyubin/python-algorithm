import sys


def chk(pw):
    flag = True
    for i in pw:
        if i in ['a', 'e', 'i', 'o', 'u']:
            break
    else:
        flag = False

    vow = 0
    con = 0
    for i in pw:
        if i in ['a', 'e', 'i', 'o', 'u']:
            vow += 1
            con = 0
        else:
            con += 1
            vow = 0

        if con >= 3 or vow >= 3:
            flag = False
            break

    st = pw[0]
    for i in range(1, len(pw)):
        if st == pw[i] and pw[i] != 'e' and pw[i] != 'o':
            flag = False
            break
        else:
            st = pw[i]

    return flag


while True:
    pw = sys.stdin.readline().rstrip()
    if pw == 'end':
        break

    if chk(pw):
        print(f'<{pw}> is acceptable.')
    else:
        print(f'<{pw}> is not acceptable.')
