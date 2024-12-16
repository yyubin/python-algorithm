import sys
n = int(sys.stdin.readline())

ans = 0
ans_li = []

for i in range(1, n+1):
    tmp = 2
    tmp_li = [n, i]

    while True:
        a = tmp_li[-2] - tmp_li[-1]
        if a < 0:
            break
        else:
            tmp += 1
            tmp_li.append(a)

    if tmp > ans:
        ans = tmp
        ans_li = tmp_li

print(ans)
print(*ans_li)
