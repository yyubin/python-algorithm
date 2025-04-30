import sys
n, m = map(int, sys.stdin.readline().split())
ban = set()

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    ban.add((a, b))
    ban.add((b, a))

cnt = 0
for a in range(1, n-1):
    for b in range(a+1, n):
        if (a, b) in ban:
            continue
        for c in range(b+1, n+1):
            if (a, c) in ban or (b, c) in ban:
                continue
            cnt += 1
print(cnt)
