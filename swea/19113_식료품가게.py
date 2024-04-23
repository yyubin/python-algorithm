tc = int(input())
ans = []

for x in range(tc):
    n = int(input())
    li = list(map(int, input().split()))

    res = []
    for i in li:
        value = float(i)/0.75
        if value in li:
            if value%4 == 0:
                res.append(i)
                idx = li.index(value)
                li[idx] = -1

    res.sort()
    res.insert(0, '#'+str(x+1))
    ans.append(res)

for i in ans:
    print(*i)
