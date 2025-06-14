# 그리디만써서는 안되는듯
import sys
for _ in range(int(sys.stdin.readline())):
    n, k = map(int, sys.stdin.readline().split())
    li = list(map(int, sys.stdin.readline().split()))
    li.sort(reverse=True)
    res = 0

    while li:
        i = 0
        partner = 0
        tmp_quot, tmp_rem = 0, sys.maxsize
        now = li.pop(0)
        while i < len(li):
            quot, rem = (li[i] + now) // k, (li[i] + now) / k
            if quot > tmp_quot:
                tmp_quot, tmp_rem = quot, rem
                partner = i
                i += 1
            elif quot == tmp_quot and rem < tmp_rem:
                tmp_quot, tmp_rem = quot, rem
                partner = i
                i += 1
            else:
                li.pop(partner)
                break

        res += tmp_quot
    print(res)

