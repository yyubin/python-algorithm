import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
res_li = {}

a, b = 0, len(li)-1
while a < b:
    result = li[a] + li[b]
    if result == 0:
        res_li[abs(result)] = (li[a], li[b])
        break
    elif result > 0:
        res_li[abs(result)] = (li[a], li[b])
        b -= 1
    else:
        res_li[abs(result)] = (li[a], li[b])
        a += 1


res_li = sorted(res_li.items())
print(*res_li[0][1])