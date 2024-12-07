import sys
s = [sys.stdin.readline().rstrip() for _ in range(int(sys.stdin.readline()))]
ans = []
tmp = ''

def is_integer(n):
    try:
        int(n)
    except ValueError:
        return False
    else:
        return True

for i in s:
    for j in i:
        if is_integer(j):
            tmp += j
        else:
            if len(tmp) > 0:
                ans.append(tmp)
                tmp = ''
    if len(tmp) > 0:
        ans.append(tmp)
        tmp = ''

ans = [int(i) for i in ans]
ans.sort()
print(*ans, sep='\n')


