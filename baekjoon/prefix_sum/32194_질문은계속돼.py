import sys
input = sys.stdin.readline
N = int(input())
prefixYes = [0] * (N + 2)
prefixNo = [0] * (N + 2)

prefixYes[1] = 1
cur = 2

for _ in range(N):
    t, x, y = map(int, input().split())

    if t == 1:
        ok = (prefixYes[y] - prefixYes[x - 1] == (y - x + 1))

    else:
        ok = (prefixNo[y] - prefixNo[x - 1] == (y - x + 1))

    if ok:
        print("Yes")
        prefixYes[cur] = prefixYes[cur - 1] + 1
        prefixNo[cur] = prefixNo[cur - 1]
    else:
        print("No")
        prefixYes[cur] = prefixYes[cur - 1]
        prefixNo[cur] = prefixNo[cur - 1] + 1

    cur += 1
