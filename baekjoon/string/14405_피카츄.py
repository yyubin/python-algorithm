import sys
s = sys.stdin.readline().rstrip()
now = ''
for i in s:
    now += i
    if now in ['pi', 'ka', 'chu']:
        now = ''
if now == '':
    print('YES')
else:
    print('NO')
