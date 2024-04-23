for x in range(10):
    n = int(input())
    li = list(map(int, input().split()))
    res = 0

    for i in range(2, n-2):
        if li[i] > li[i - 1] and li[i] > li[i - 2] and li[i] > li[i + 1] and li[i] > li[i + 2]:
            res += min(abs(li[i] - li[i - 1]),
                       abs(li[i] - li[i - 2]),
                       abs(li[i] - li[i + 1]),
                       abs(li[i] - li[i + 2]))

    print('#' + str(x + 1), res)
