import sys

string = sys.stdin.readline().rstrip()
li = list(string)
tmp_li = list(string.split('.'))
result = []


def check():
    for i in tmp_li:
        if len(i) % 2 != 0:
            print(-1)
            return False
    return True


li.append(';')
cnt = 1
if check():
    for i in range(len(li) - 1):
        if li[i] == '.':
            result.append('.')
            cnt = 1
        else:
            if cnt == 4:
                result.append('AAAA')
                cnt = 1
            elif cnt == 2 and li[i + 1] != 'X':
                result.append('BB')
                cnt = 1
            else:
                cnt += 1

    print(*result, sep="")
