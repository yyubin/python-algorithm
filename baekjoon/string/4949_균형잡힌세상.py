import sys
while True:
    string = sys.stdin.readline().rstrip()
    if string == '.':
        break

    li = []
    for i in string:
        if i in ['(', '[', ')', ']']:
            li.append(i)

    tmp = ''.join(li)

    for _ in range(len(li)//2):
        tmp = tmp.replace('()', '')
        tmp = tmp.replace('[]', '')

    print('no' if len(tmp) > 0 else 'yes')


