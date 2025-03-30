import sys
for _ in range(int(sys.stdin.readline())):
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    max_ = max(b)
    res = 0
    for i in range(k):
        if i < n:
            res += a[i]
        else:
            res += max_
        print(res)

    print("0---")

    print(res)


# 4 7
# 4 3 1 2
# 1 1 1 1

# 1 2 7 3 -> 13