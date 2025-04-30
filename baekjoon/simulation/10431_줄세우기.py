import sys
p = int(sys.stdin.readline())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(p)]

def sorting(lst):
    res = 0
    for i in range(20):
        now = lst[i]
        for j in range(i):
            if lst[j] > now:
                lst.pop(i)
                lst.insert(j, now)
                res += (i-j)
                break

    return res

for i in range(p):
    idx = li[i].pop(0)
    print(idx, sorting(li[i]))
