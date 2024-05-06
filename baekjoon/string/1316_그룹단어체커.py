import sys
n = int(sys.stdin.readline())
li = [sys.stdin.readline().rstrip() for _ in range(n)]
cnt = n

for i in li:
    now = i[0]
    chk = []
    for j in list(i):
        if j not in chk or j == now:
            chk.append(j)
            now = j
        else:
            cnt -= 1
            break

print(cnt)
