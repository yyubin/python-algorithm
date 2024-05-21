import sys
l, r = map(str, sys.stdin.readline().split())

if l.count('8') == r.count('8') == 0 or len(l) != len(r):
    print(0)
    sys.exit()

ans = 0
for i in range(len(r)):
    if l[i] == r[i] == '8':
        ans += 1
    elif l[i] == r[i]:
        continue
    else:
        break

print(ans)
