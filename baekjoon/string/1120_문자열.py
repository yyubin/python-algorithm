import sys
a, b = map(str, sys.stdin.readline().rstrip().split())

ans = 0
idx = 0
for i in range(len(b)-len(a)+1):
    tmp = b[i:len(a)+i]
    tmp_cnt = 0
    for j in range(len(a)):
        if a[j] == tmp[j]:
            tmp_cnt += 1

    if ans < tmp_cnt:
        ans = tmp_cnt
        idx = i

print(len(a) - ans)
