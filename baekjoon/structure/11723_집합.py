import sys
cnt = int(sys.stdin.readline())
s = set([])

while cnt > 0:
    li = list(sys.stdin.readline().rstrip().split())
    if li[0] == 'add':
        s.add(li[1])
    elif li[0] == 'remove':
        if li[1] in s:
            s.remove(li[1])
    elif li[0] == 'check':
        if li[1] in s:
            print(1)
        else:
            print(0)
    elif li[0] == 'toggle':
        if li[1] in s:
            s.remove(li[1])
        else:
            s.add(li[1])
    elif li[0] == 'all':
        tmp = [str((i+1)) for i in range(20)]
        s = set(tmp)
    elif li[0] == 'empty':
        s = set([])

    cnt -= 1
