import sys
s = list(sys.stdin.readline())
ucpc = ['U', 'C', 'P', 'C']
ck = [False] * 4
idx = 0
for v in s:
    if v[0] == ucpc[idx]:
        ck[idx] = True
        idx += 1
    if idx > 3:
        break

print('I love UCPC' if False not in ck else 'I hate UCPC')
