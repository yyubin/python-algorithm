import sys
n = int(sys.stdin.readline())
res = 0
for i in range(1, n+1):
    tmp = [int(x) for x in list(str(i))]
    if len(tmp) <= 2:
        res += 1
        continue

    diff = tmp[1] - tmp[0]
    for j in range(1, len(tmp)):
        if tmp[j] - tmp[j-1] != diff:
            break
    else:
        res += 1

print(res)

